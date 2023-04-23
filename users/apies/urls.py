from rest_framework import routers

from . import api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserAPIViewSet, basename='users')

urlpatterns = [

]

urlpatterns += router.urls
