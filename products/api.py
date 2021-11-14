from products.models import Product
from rest_framework import viewsets, permissions
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions = [permissions.AllowAny]
