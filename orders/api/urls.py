from rest_framework import routers

from . import api_views

router = routers.DefaultRouter()
router.register(r'orders', api_views.OrderAPIViewSet,
                basename='orders')  # Отображение api всех заказов
router.register(r'orders_paid', api_views.OrderPaidAPIViewSet,
                basename='orders_paid')  # Отображение api оплаченных заказов

urlpatterns = [

]

urlpatterns += router.urls
