from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', view=views.product_list, name='product_list'),
    # path('', view=views.ProductList.as_view(), name='product_list'),
    path('<slug:category_slug>/', view=views.product_list, name='product_list_by_category'),
    # path('<slug:category_slug>/', view=views.ProductList.as_view(), name='product_list_by_category')
    path('<int:id>/<slug:product_slug>/', view=views.product_detail, name='product_detail'),


]
