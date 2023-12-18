import graphene
from graphene_django import DjangoObjectType
from .models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields=("productId","productName","productDescription","listPrice","slaesPrice","productImage","productStock","productFeatures","currency")
    listPrice = graphene.Float()

    def resolve_listPrice(self, info):
        return float(self.listPrice)
    slaesPrice = graphene.Float()

    def resolve_slaesPrice(self, info):
        return float(self.slaesPrice)

from .mutations import(
    createProduct,
    delete
)



class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    product = graphene.Field(ProductType, productId = graphene.ID())
    

    def resolve_products(root,info):
        return Product.objects.all()
    
    def resolve_product(root,info, productId):
        return Product.objects.get(productId = productId)

    


class Mutation(graphene.ObjectType):
    createProduct = createProduct.Field()
    delete = delete.Field()



schema = graphene.Schema(query = Query, mutation=Mutation)