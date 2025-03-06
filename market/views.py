from rest_framework import viewsets
from .models import Product, Service
from .serializers import ProductSerializer, ServiceSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """CRUD para produtos do marketplace"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    """CRUD para serviços do marketplace"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
