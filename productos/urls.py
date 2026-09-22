from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    CategoriaViewSet,
    MarcaViewSet,
    ProductoViewSet
)


router = DefaultRouter()

router.register(
    'categorias',
    CategoriaViewSet
)

router.register(
    'marcas',
    MarcaViewSet
)

router.register(
    'productos',
    ProductoViewSet
)


urlpatterns = [
    path('', include(router.urls))
]