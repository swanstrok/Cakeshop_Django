from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', view=views.product_list, name='product_list'),
    path('<slug:category_slug>/', view=views.product_list, name='product_list_by_category'),

]
