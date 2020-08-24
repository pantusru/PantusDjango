from django.urls import path
from .views import NewsListView
from .views import NewsDetail
from .views import NewsCategoryList
from .views import help
from .views import GetNewsForCategory
from .views import ProductCategoryList
from .views import ProductApplicabilitiesList
from .views import ProductApplicabilitiesDetail


urlpatterns = [
    path('news/', NewsListView().as_view()),  # список новостей
    path('news/detail/', NewsDetail().as_view()),  # детали статьи
    path('news/category/', GetNewsForCategory().as_view()),  #  вывод статей конкретной категории
    path('news/category/list', NewsCategoryList().as_view()),  # список категорий

    path('catalog/category/list', ProductCategoryList().as_view()),
    path('catalog/applicabilities/list', ProductApplicabilitiesList().as_view()),
    path('catalog/applicabilities/', ProductApplicabilitiesDetail().as_view()),

    path('help', help),  # хелпа по апи
]