from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NewsListSerializer
from news.models import News
from .serializers import NewsDetailSerializer
from news.models import NewsCategory
from .serializers import NewsCategorySerializer


# Create your views here.

class NewsListView(APIView, LimitOffsetPagination):
    """Вывод списка новостей
    news/?limit=10&offset=0
    """

    def get (self, request):
        newses = News.objects.all().order_by('-id')
        results = self.paginate_queryset(newses, request, view=self)
        serializer = NewsListSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)


class NewsDetail (APIView):
    """Вывод полной инф. по статье
    news/detail/?id=100
    """

    def get(self, request):
        id = request.GET['id']
        try:
            snippet = News.objects.get(id=id)
        except News.DoesNotExist:
            return HttpResponse(status=201)

        if request.method == 'GET':
            serializer = NewsDetailSerializer(snippet)
            return Response(serializer.data)


class NewsCategoryList (APIView):
    """Список категорий
    news/category/list
    """

    def get (self, request):
        newscategory = NewsCategory.objects.all()
        serializer = NewsCategorySerializer(newscategory, many=True)
        return Response(serializer.data)


class GetNewsForCategory(APIView):
    """ Вывод статей по категории
    news/category/?id=4
    """

    def get(self, request):
        id = request.GET['id']
        try:
            snippet = News.objects.all().filter(category_id=id)
        except News.DoesNotExist:
            return HttpResponse(status=201)
        if request.method == 'GET':
            serializer = NewsDetailSerializer(snippet, many=True)
            return Response(serializer.data)




"""
==================== PAGES ======================
"""

def help(request):
    """Страничка хелпы по апи"""
    return render(request, 'help.html')