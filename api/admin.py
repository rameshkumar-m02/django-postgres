from django.contrib import admin
from .resources import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class  =   ProductAdminResource