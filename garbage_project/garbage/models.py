from django.db import models

class GarbageCategory(models.Model):
    name = models.CharField(max_length=50)  # 例：燃えるゴミ、プラスチック、紙など

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)  # 例：札幌市、渋谷区

    def __str__(self):
        return self.name


class CityCategoryName(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(GarbageCategory, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)  # 地域での呼び名（例：プラゴミ）

    def __str__(self):
        return f"{self.city.name} - {self.display_name}"