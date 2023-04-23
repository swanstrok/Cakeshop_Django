from django.db import models
from shop.models import Product


# Create your models here.
class Order(models.Model):
    """Модель заказа"""
    name = models.CharField(max_length=200, verbose_name="Имя")
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время оформления')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачен')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order №{self.id}'


class OrderProduct(models.Model):
    """Модель каждого продукта в заказе"""
    order = models.ForeignKey(to='Order', related_name='items', on_delete=models.CASCADE,
                              verbose_name='Заказ')
    product = models.ForeignKey(to=Product, related_name='order_products', on_delete=models.CASCADE,
                                verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.id}'
