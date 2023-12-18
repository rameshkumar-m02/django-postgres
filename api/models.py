from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    productDescription = models.CharField(max_length=240)
    listPrice =  models.FloatField(verbose_name="listPrice",default=0.0)
    slaesPrice = models.FloatField(verbose_name="slaesPrice",default=0.0)
    productImage = models.CharField(max_length=240)
    productStock = models.CharField(max_length=240)
    productFeatures = models.CharField(max_length=240)
    currency = models.CharField(max_length=240)
    
