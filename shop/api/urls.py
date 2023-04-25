from django.urls import path
from rest_framework import routers

from . import api_views

router = routers.DefaultRouter()
router.register(r'product', api_views.ProductAPIViewSet, basename='product')
router.register(r'product_category', api_views.CategoryAPIViewSet, basename='product_category')

urlpatterns = [

]

urlpatterns += router.urls
