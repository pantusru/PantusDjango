
from django.urls import path
from rest_framework import routers

from .views import NewsListView
from .views import NewsDetail
from .views import NewsCategoryList
from .views import help
from .views import GetNewsForCategory



# router = routers.DefaultRouter(trailing_slash=False)
#
# router.register('country', CountryViewSet, base_name='country')
# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]


urlpatterns = [

    path('news/', NewsListView().as_view()),
    path('news/detail/', NewsDetail().as_view()),
    path('news/category/', GetNewsForCategory().as_view()),
    path('news/category/list', NewsCategoryList().as_view()),
    #path('test', AdvancedCreateAtNewsSerializer.get_create_at),

    path('help', help),

]