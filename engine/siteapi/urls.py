from django.urls import path
from .views import NewsListView
from .views import NewsDetail
from .views import NewsCategoryList
from .views import help
from .views import GetNewsForCategory
from .views import CategoryListAPI


urlpatterns = [
    path('news/', NewsListView().as_view()),  # список новостей
    path('news/detail/', NewsDetail().as_view()),  # детали статьи
    path('news/category/', GetNewsForCategory().as_view()),  #  вывод статей конкретной категории
    path('news/category/list', NewsCategoryList().as_view()),  # список категорий
    #path('catalog/category/list', CategoryListAPI().as_view()),  # список категорий
    path('catalog/category/list', CategoryListAPI().as_view()),
    # path('catalog/category/list/<int:pk>', CategoryListAPI.as_view({'get': 'retrieve'})),
    path('help', help),  # хелпа по апи
]