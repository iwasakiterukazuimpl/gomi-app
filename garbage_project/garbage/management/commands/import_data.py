import csv
from django.core.management.base import BaseCommand
from garbage.models import City, GarbageCategory, CityCategoryName

class Command(BaseCommand):
    help = 'CSVファイルから市区町村・ごみ分類データをインポートします。'

    def handle(self, *args, **options):
        # City
        with open('cities.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                City.objects.get_or_create(name=row['name'])
        self.stdout.write(self.style.SUCCESS('✅ City インポート完了'))

        # GarbageCategory
        with open('garbage_categories.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                GarbageCategory.objects.get_or_create(name=row['name'])
        self.stdout.write(self.style.SUCCESS('✅ GarbageCategory インポート完了'))

        # CityCategoryName
        with open('city_category_names.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                city = City.objects.get(name=row['city'])
                category = GarbageCategory.objects.get(name=row['category'])
                CityCategoryName.objects.get_or_create(
                    city=city,
                    category=category,
                    defaults={'display_name': row['display_name']}
                )
        self.stdout.write(self.style.SUCCESS('✅ CityCategoryName インポート完了'))