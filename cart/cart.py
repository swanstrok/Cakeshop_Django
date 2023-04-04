from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:

    def __init__(self, request):
        """Инициализация корзины"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Если в сессии отсутствует корзина, то мы создадим сессию с пустой корзиной #
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """Итерируется по объектам в корзине и достает продукты из нашей БД"""
        product_ids = self.cart.keys()
        # Достает все объекты продуктов и добавляет их в корзину
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def save(self):
        """Оценивает сессию как 'измененную' для того чтобы убедиться что она сохранилась"""
        self.session.modified = True

    def add(self, product, quantity=1, update_quantity=False):
        """Добавление товара в корзину или обновление его количества"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """Удаляет продукт с корзины"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Удаляем корзину из сессии"""
        del self.session[settings.CART_SESSION_ID]
        self.save()
