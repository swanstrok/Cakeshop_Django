from django.urls import path, include
from . import views

app_name = 'orders'

urlpatterns = [
    path('', view=views.order_add, name='order_add'),
]
