import graphene
from graphene_django import DjangoObjectType
#from graphene_django.filter import DjangoFilterConnectionField
from .models import Product

class ProductClass(DjangoObjectType):
    class Meta:
        model = Product
