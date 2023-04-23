from rest_framework import routers

from . import api_views


router = routers.DefaultRouter()
router.register(r'orders', api_views.OrderAPIViewSet, basename='orders')
router.register(r'orders_paid', api_views.OrderPaidAPIViewSet, basename='orders_paid')

urlpatterns = [

]

urlpatterns += router.urls
