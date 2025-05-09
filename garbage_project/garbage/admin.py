from django.contrib import admin
from .models import GarbageCategory, City, CityCategoryName

admin.site.register(GarbageCategory)
admin.site.register(City)
admin.site.register(CityCategoryName)