from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import NewsListSerializer
from controlcore.models import News
from .serializers import NewsDetailSerializer
from controlcore.models import NewsCategory
from .serializers import NewsCategorySerializer


# Create your views here.




class NewsListView(APIView, LimitOffsetPagination):
    """Вывод списка новостей"""

    def get (self, request):
        newses = News.objects.all().order_by('-id')
        results = self.paginate_queryset(newses, request, view=self)
        serializer = NewsListSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)


class NewsDetail (APIView):
    """Вывод полной инф. по новости"""

    def get(self, request):
       # print(f'YA TUT')

        id = request.GET['id'] #http://127.0.0.1:8000/api/v1/news/detail/?id=903
        try:
            snippet = News.objects.get(id=id)
        except News.DoesNotExist:
            return HttpResponse(status=201)

        if request.method == 'GET':
            serializer = NewsDetailSerializer(snippet)
            return Response(serializer.data)



class NewsCategoryList (APIView):
    """Список категорий"""
    def get (self, request):
        newscategory = NewsCategory.objects.all()
        serializer = NewsCategorySerializer(newscategory, many=True)
        return Response(serializer.data)






"""PAGES"""

def help(request):
    return render(
        request,
        'help.html',
    )

class GetNewsForCategory(APIView):

    def get(self, request):


        id = request.GET['id']  # http://127.0.0.1:8000/api/v1/news/category/?id=4
        try:
            snippet = News.objects.all().filter(category_id=id)
        except News.DoesNotExist:
            return HttpResponse(status=201)

        if request.method == 'GET':
            serializer = NewsDetailSerializer(snippet, many=True)
            return Response(serializer.data)


# class AdvancedCreateAtNewsSerializer (APIView):
#
#
#
#     def get_create_at(self, request):
#             # This kind of method should be like get_<fieldYouWantToGet>()
#
#         print('ddfffffffffffffffffffffffffffffffffff')
#         #return News.nickname