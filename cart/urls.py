from django.urls import path
from .views import cart_add, cart_detail, cart_remove

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),  # Отображение корзины
    path('add/<int:product_id>/', cart_add,  # Добавление товара в корзину
         name='cart_add'),
    path('remove/<int:product_id>/', cart_remove,  # Удаление товара из корзины
         name='cart_remove'),
]
