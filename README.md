# ごみ出しアプリ（Gomi App）

このアプリは、カメラと位置情報を使ってごみの種類を判別するAIアプリです。

## 🔽 クローン方法

```bash
git clone https://github.com/iwasakiterukazuimpl/gomi-app.git
cd gomi-app
```

## ⚙️ セットアップ手順（Python）

1. 仮想環境を作成して有効化：

```bash
python3 -m venv venv
source venv/bin/activate
```

2. 依存パッケージをインストール：

```bash
pip install -r requirements.txt
```

3. アプリを起動：

```bash
streamlit run app.py
```

## 📦 主な使用ライブラリ

- streamlit
- torch
- torchvision
- Pillow
- geopy

## 📍 特徴

- Webカメラから画像を取得
- 位置情報（GPS）を自動で取得
- AIでごみの種類を分類（例：可燃ごみ、プラスチックなど）

## 📸 注意点

このアプリではブラウザ上で位置情報とカメラの利用が必要です。実行時に許可を求められたら「許可」を選んでください。