from django.contrib import admin
from .models import Order, OrderProduct


# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct


@admin.register(Order)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email', 'phone', 'address', 'created', 'is_paid']
    list_filter = ['is_paid', 'created']
    inlines = [OrderProductInline]
