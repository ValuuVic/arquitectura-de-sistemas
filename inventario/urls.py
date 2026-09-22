from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    BodegaViewSet,
    MovimientoInventarioViewSet,
    InventarioProductoViewSet
)


router = DefaultRouter()


router.register(
    'bodegas',
    BodegaViewSet
)


router.register(
    'movimientos',
    MovimientoInventarioViewSet
)


router.register(
    'inventario',
    InventarioProductoViewSet
)


urlpatterns = [
    path('', include(router.urls))
]