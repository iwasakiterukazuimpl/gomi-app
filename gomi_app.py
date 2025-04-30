import streamlit as st
from PIL import Image
import torch
import torchvision.models as models
from torchvision import transforms
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import json
import time

# モデル構造を定義（あなたが学習時に使った構造と同じにする）
model = torch.load("full_model.pth", weights_only=False)
model.eval()

default_classes = ["燃えるごみ", "プラスチック", "ペットボトル", "ダンボール"]

#jsonから分別データを読み込む
with open("area_class_map.json", encoding="utf-8") as f:
    area_class_map = json.load(f)

# --- 軽量前処理 ---
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# --- Streamlit UI ---
st.title("ごみ分類AI")
st.markdown("画像からごみの種類を判定します 🧠🗑️")

# --- GPS位置情報取得 ---
st.markdown("### 位置情報の取得")
st.markdown("位置情報の取得を許可してください。より正確なごみ分別情報を提供するために使用します。")

js_code = """
<script>
navigator.geolocation.getCurrentPosition(
    (position) => {
        const coords = position.coords.latitude + "," + position.coords.longitude;
        const input = window.parent.document.querySelector('input[data-testid="stTextInput"]');
        const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        nativeInputValueSetter.call(input, coords);
        input.dispatchEvent(new Event('input', { bubbles: true }));
    }
);
</script>
"""

st.markdown("位置情報を取得して分類名を地域別に変換します。")
st.markdown("※ブラウザに位置情報の許可が必要です。")

# テキストボックスに自動で座標を入れる
st.components.v1.html(js_code, height=0)
coords = st.text_input("現在位置（緯度,経度）")

# デフォルトの地域名を設定
city_name = "Unknown"

if coords:
    try:
        lat, lon = map(float, coords.split(","))
        geolocator = Nominatim(user_agent="my_gomi_app")

        time.sleep(1)  # Nominatimへの連続アクセス回避

        location = geolocator.reverse((lat, lon), language='ja')
        address = location.raw.get('address', {})
        city_name = address.get("city") or address.get("town") or address.get("state") or "不明"

        st.success(f"📍 現在地推定: **{city_name}**")
    except Exception as e:
        st.error("位置情報の取得に失敗しました。")
        st.exception(e)

# --- カメラ入力 ---
camera_image = st.camera_input("写真を撮影してください")
image = None

if camera_image is not None:
    image = Image.open(camera_image).convert("RGB")
    st.image(image, caption="撮影された画像", use_container_width=True)

# --- 推論と表示 ---
if image:
    input_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
        pred_idx = torch.argmax(output, dim=1).item()
        raw_class = default_classes[pred_idx]

    if city_name in area_class_map:
        class_name = area_class_map[city_name].get(raw_class, raw_class)
    else:
        class_name = raw_class

    st.success(f"🧠 推論結果: **{class_name}**（元の分類: {raw_class}）")
