# Generated by Django 3.2 on 2023-04-04 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время оформления'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Оплачен'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='surname',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='shop.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
    ]