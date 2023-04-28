from django.urls import path, include

from . import views

app_name = 'shop'

urlpatterns = [
    path('', view=views.product_list, name='product_list'),  # Отображение всей продукции
    path('<slug:category_slug>/', view=views.product_list, name='product_list_by_category'),
    # Отображение всей по выбранной категории
    path('<int:id>/<slug:product_slug>/', view=views.product_detail, name='product_detail'),
    # Отображение выбранного товара

]
