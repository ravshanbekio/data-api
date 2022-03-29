from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoydalanuvchiViewSet, ProductViewSet, StatsViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('user',FoydalanuvchiViewSet, basename='users')
router.register('products',ProductViewSet, basename='products')
router.register('stats',StatsViewSet, basename='stats')

schema_view = get_schema_view(
   openapi.Info(
      title="Data API",
      default_version='v1',
      description="",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Ravshanbek Madaminov <ravshanbekmadaminov68@gmail.com> <+998903036415>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',include(router.urls)),
    path('documentation/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('documentation/redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
]