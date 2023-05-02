from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .yasg import urlpatterns as swag_urls

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT обновление
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # JWT подтверждение
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT получение
    path('api/drf-auth/', include('rest_framework.urls')),  # Авторизация по сессиям DRF
    path('api/users/', include('users.api.urls')),  # api со списком информации о пользователях
    path('api/orders/', include('orders.api.urls')),  # api со списком информации о заказах
    path('api/', include('shop.api.urls')),  # api со списком информации о товарах
    path('cart/', include('cart.urls', namespace='cart')),  # url связанный с cart-app
    path('orders/', include('orders.urls', namespace='orders')),  # url связанный с orders-app
    path('accounts/', include('users.urls')),  # url связанный с users-app
    path('', include('shop.urls', namespace='shop')),  # url связанный с shop-app
]

# Добавление swagger-urls к urls (Через цикл т.к происходит конфликт из-за пустого пути к shop.urls)
for i in swag_urls:
    urlpatterns.insert(1, i)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
