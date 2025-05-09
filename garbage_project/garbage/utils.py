# garbage/utils.py

from .models import City, GarbageCategory, CityCategoryName

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