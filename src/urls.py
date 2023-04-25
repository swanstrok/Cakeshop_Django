from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/users/', include('users.api.urls')),
    path('api/orders/', include('orders.api.urls')),
    path('api/', include('shop.api.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('accounts/', include('users.urls')),
    path('', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
