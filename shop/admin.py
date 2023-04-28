from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Регистрация в админке модели Product"""
    list_display = ['category', 'name', 'slug', 'image_show', 'description', 'price', 'stock',
                    'available', 'created', 'updated']
    list_filter = ['created', 'updated', 'available']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        """Функция для отображения в админке изображения товара а не его url"""
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Регистрация в админке модели Category"""
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
