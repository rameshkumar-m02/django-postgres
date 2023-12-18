from django.shortcuts import render
from rest_framework import viewsets
from api.models import Product
from api.serializers import ProductSerializers
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers