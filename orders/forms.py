from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """Форма для оформления заказа"""
    class Meta:
        model = Order
        fields = ['name', 'surname', 'email', 'phone', 'address']
