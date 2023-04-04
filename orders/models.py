from django.db import models
from shop.models import Product


# Create your models here.
class Order(models.Model):
    """Модель заказа"""
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order №{self.id}'