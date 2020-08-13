from django.urls import path
from .views import *
from .db_api_methods.import_product_category import ImportProductCategory

urlpatterns = [
path('get', getiing, name='test'),
path('product/category', ImportProductCategory().insert_table_catalog_productcategory)
]