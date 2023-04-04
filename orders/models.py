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


class OrderProduct(models.Model):
    """Модель каждого продукта в заказе"""
    order = models.ForeignKey(to='Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, related_name='order_products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.id}'