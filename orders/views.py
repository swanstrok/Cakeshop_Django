from django.shortcuts import render
from .models import *
from cart.cart import Cart
from .forms import OrderCreateForm


# Create your views here.
def order_add(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderProduct.objects.create(order=order,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])

            cart.clear()

            return render(request,
                          template_name='orders/order/created.html',
                          context={'order': order})

    else:
        form = OrderCreateForm()

    return render(request,
                  template_name='orders/order/create.html',
                  context={'cart': cart,
                           'form': form})
