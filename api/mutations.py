import graphene
from graphene_file_upload.scalars import Upload
from .fields import(
    ProductClass,
)
from .models import (
    Product,
)

class createProduct(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    product = graphene.Field(ProductClass)

    class Meta:
        description = "Add Product details"
        
    class Arguments:
        productId =  graphene.String()
        productName =  graphene.String(required=True)
        productDescription =  graphene.String(required=False)
        listPrice = graphene.Float(required=True)
        slaesPrice = graphene.Float(required=True)
        productImage = graphene.String(required=False)
        productStock = graphene.String(required=False)
        productFeatures = graphene.String(required=False)
        currency = graphene.String(required=False)

    def mutate(self,info, **kwargs):
        try:
            product = Product.objects.create(
                productId = kwargs.get("productId"),
                productName = kwargs.get("productName"),
                productDescription = kwargs.get("productDescription"),
                listPrice = kwargs.get("listPrice"),
                slaesPrice = kwargs.get("slaesPrice"),
                productImage = kwargs.get("productImage"),
                productStock = kwargs.get("productStock"),
                productFeatures = kwargs.get("productFeatures"),
                currency = kwargs.get("currency"),
                )
           
            return createProduct(product = product, success = True)
        except Exception as e:
            print("ERROR",e)
            return createProduct(product = None, success = False, error = e)


class delete(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    
    class Arguments:
        product_id = graphene.ID()
        

    def mutate(self, info, **kwargs):
        try:
            if(kwargs.get('productId')):
                Product.objects.filter(id = kwargs.get('productId')).delete()
           
            return delete(success = True)
        except Exception as e:
            return delete(success= False, error = e)