from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    OrdenCompraViewSet,
    DetalleOrdenViewSet,
    FacturaViewSet
)


router = DefaultRouter()


router.register(
    'ordenes',
    OrdenCompraViewSet
)


router.register(
    'detalles',
    DetalleOrdenViewSet
)


router.register(
    'facturas',
    FacturaViewSet
)


urlpatterns = [
    path('', include(router.urls))
]