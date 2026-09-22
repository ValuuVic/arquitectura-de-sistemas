from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ProveedorViewSet,
    ServicioProveedorViewSet,
    ContratoProveedorViewSet
)


router = DefaultRouter()


router.register(
    'proveedores',
    ProveedorViewSet
)


router.register(
    'servicios',
    ServicioProveedorViewSet
)


router.register(
    'contratos',
    ContratoProveedorViewSet
)


urlpatterns = [
    path('', include(router.urls))
]