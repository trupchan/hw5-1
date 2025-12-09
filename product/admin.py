from django.contrib import admin
from .models import Category, Product, Review

# Регистрируем модели
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)

