from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.

@require_POST
@login_required
def cart_add(request, product_id):
    """Функция добавления товара в корзину"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect(to='cart:cart_detail')


@login_required
def cart_remove(request, product_id):
    """Функция удаления товара из корзины"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(to='cart:cart_detail')


@login_required
def cart_detail(request):
    """Функция отображения корзины"""
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})

    return render(request, template_name='cart/detail.html', context={'cart': cart})
