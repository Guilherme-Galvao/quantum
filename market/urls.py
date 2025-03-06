from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ServiceViewSet

# Criando roteador para as APIs
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas do Django REST Framework
]
