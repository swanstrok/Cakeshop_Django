from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from cart.forms import CartAddProductForm
from .models import Category, Product


# Create your views here.

# class ProductList(ListView):
#     model = Product
#     template_name = 'shop/product/list.html'
#     context_object_name = 'products'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         if self.kwargs['category_slug']:
#             context['category'] = get_object_or_404(Category, slug=self.kwargs['category_slug'])
#         else:
#             context['category'] = None
#         return context
#
#     def get_queryset(self):
#         if self.kwargs['category_slug']:
#             return Product.objects.filter(available=True, category__slug=self.kwargs['category_slug'])
#         else:
#             return Product.objects.filter(available=True)

def product_list(request, category_slug=None):
    """Функция отображает список доступных товаров"""
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, available=True)
    else:
        category = None
        products = Product.objects.filter(available=True)

    context = {'category': category,
               'categories': categories,
               'products': products}

    return render(request, template_name='shop/product/list.html', context=context)


def product_detail(request, id, product_slug):
    """Функция для детального отображения товара"""
    product = get_object_or_404(Product, id=id, slug=product_slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }

    return render(request, template_name='shop/product/detail.html', context=context)
