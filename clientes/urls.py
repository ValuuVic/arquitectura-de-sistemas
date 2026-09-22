from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ClienteViewSet,
    DireccionViewSet,
    ContactoViewSet
)


router = DefaultRouter()

router.register(
    'clientes',
    ClienteViewSet
)

router.register(
    'direcciones',
    DireccionViewSet
)

router.register(
    'contactos',
    ContactoViewSet
)


urlpatterns = [
    path('', include(router.urls))
]