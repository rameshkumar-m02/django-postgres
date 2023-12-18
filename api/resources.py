from import_export import resources
from .models import Product

class ProductAdminResource(resources.ModelResource):

    class Meta:
        model   =   Product
        import_id_fields = ('productId', )