# 🧹 ごみ分類アプリ（Django）

このアプリは、「共通ごみカテゴリ名（例：燃えるゴミ）」を、「自治体ごとのローカル名称（例：可燃ごみ）」に変換する機能を提供します。

---

## 📦 環境セットアップ手順

### 1. Python仮想環境の作成・有効化

```bash
python3 -m venv venv
source venv/bin/activate

### 2. 必要パッケージのインストール

```bash
pip install django

### 3. マイグレーション実行（データベース構築）

```bash
python manage.py makemigrations
python manage.py migrate

### 4. 管理ユーザーの作成

```bash 
python manage.py createsuperuser

### 5. 開発サーバーの起動

```bash
python manage.py runserver

---

## 🧱 モデル概要

class City(models.Model):
    name = models.CharField(max_length=100)

class GarbageCategory(models.Model):
    name = models.CharField(max_length=100)  # 共通カテゴリ名

class CityCategoryName(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(GarbageCategory, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)  # 自治体ごとの名称

---

## 💡 使用方法（Pythonスクリプト・シェル内）

### ヘルパー関数（utils.py）

def get_local_garbage_name(city_name, common_category_name):
    try:
        city = City.objects.get(name=city_name)
    except City.DoesNotExist:
        return f"{city_name} は登録されていません。"

    try:
        category = GarbageCategory.objects.get(name=common_category_name)
    except GarbageCategory.DoesNotExist:
        return f"{common_category_name} は共通分類として登録されていません。"

    try:
        mapping = CityCategoryName.objects.get(city=city, category=category)
        return mapping.display_name
    except CityCategoryName.DoesNotExist:
        return f"{city_name} に {common_category_name} の分類名は登録されていません。"

### 実行例（Djangoシェル）

```bash
python manage.py shell

from garbage.utils import get_local_garbage_name
get_local_garbage_name("札幌市", "燃えるゴミ")
# → "可燃ごみ"


## 🔧 管理画面（データ登録）
http://127.0.0.1:8000/admin にアクセスして、以下を登録します：

City（例：札幌市）

GarbageCategory（例：燃えるゴミ）

CityCategoryName：上記2つを結びつけ、表示名を登録（例：「可燃ごみ」）


## 🧑‍💻 開発環境
Python 3.13（推奨 3.10 以上）

Django 4.x

SQLite3（開発用）
