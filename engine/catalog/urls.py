from django.urls import path

from . import admin
from .views import *
from .db_api_methods.import_product_category import ImportProductCategory
from .db_api_methods.import_product_applicabilities import ImportProductApplicabilities




urlpatterns = [
path('get', getiing, name='test'),
path('product/category', ImportProductCategory().insert_table_catalog_productcategory),
path('product/applicabilities', ImportProductApplicabilities().insert_table_catalog_productapplicabilities),
]

