from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .urls import urlpatterns as original_patterns

urlpatterns = [
    path('api/auth/login/', TokenObtainPairView.as_view(), name='jwt_login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('api/auth/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
    *original_patterns,
]
