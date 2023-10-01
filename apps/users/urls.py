from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.app.views import *
from apps.users.views import *
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('protype',ProTypeViewSet)
router.register('image',ImageViewSet)
router.register('service',ServiceViewSet)
router.register('master',MasterViewSet)
router.register('image-service',ImageServiceViewSet)

# router.register('customer', CustomerViewset, basename='customer')
router.register('seller', SellerViewset, basename='seller')

urlpatterns = [
    path('', include(router.urls)),
    path('auth-token/', obtain_auth_token, name='api_token_auth'),
    
]