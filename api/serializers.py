from rest_framework import serializers
from api.models import Product

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    #product_id=serializers.ReadOnlyField()
    class Meta:
        model=Product
        fields="__all__"
        