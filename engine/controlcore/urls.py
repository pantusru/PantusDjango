from django.urls import path, include
from .db_api_methods.import_popular_product import create_new_product
from .site_api_methods.news import get_news
from .db_api_methods.import_news_data import importNewsData



urlpatterns = [
path('db/api/test', create_new_product, name='test'),

path('db/api/getnews', importNewsData, name='getnews'),

path('web/api/getnews', get_news, name='test'),


]
