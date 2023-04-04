from django.shortcuts import render, get_object_or_404

from .models import Category, Product


# Create your views here.

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
