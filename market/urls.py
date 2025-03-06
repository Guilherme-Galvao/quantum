from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ServiceViewSet
from .views import ProductList, ProductDetail, ServiceList, ServiceDetail


# Criando roteador para as APIs
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas do Django REST Framework
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
]
