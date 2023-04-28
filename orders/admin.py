from django.contrib import admin
from .models import Order, OrderProduct


# Register your models here.
class OrderProductInline(admin.TabularInline):
    """Делает табуляр модели OrderProduct для связи с таблицей Order"""
    model = OrderProduct


@admin.register(Order)
class OrderProductAdmin(admin.ModelAdmin):
    """Регистрация модели Order в админке"""
    list_display = ['id', 'name', 'surname', 'email', 'phone', 'address', 'created', 'is_paid']
    list_filter = ['is_paid', 'created']
    inlines = [OrderProductInline]
