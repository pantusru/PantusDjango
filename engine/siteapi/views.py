import json

from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from mptt.templatetags.mptt_tags import cache_tree_children
from psycopg2.extensions import JSON

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import NewsListSerializer, User, UserSerializer
from news.models import News
from .serializers import NewsDetailSerializer
from news.models import NewsCategory
from .serializers import NewsCategorySerializer
from catalog.models import ProductCategory
from catalog.models import ProductApplicabilities



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


class GetNewsForCategory(APIView, LimitOffsetPagination):
    """ Вывод статей по категории
    news/category/?id=4&limit=10&offset=0
    """

    def get(self, request):
        id = request.GET['id']
        try:
            snippet = News.objects.all().filter(category_id=id)
        except News.DoesNotExist:
            return HttpResponse(status=201)
        if request.method == 'GET':
            results = self.paginate_queryset(snippet, request, view=self)
            serializer = NewsDetailSerializer(results, many=True)
            return Response(serializer.data)


class ProductCategoryList(APIView):
    """Категории продуктов"""

    def get (self, request):
        root_nodes = cache_tree_children(ProductCategory.objects.all())
        dicts = []
        for n in root_nodes:
            dicts.append(self.recursive_node_to_dict(n))
        return Response(dicts)

    def recursive_node_to_dict(self, node):
        result = {
            'id': node.pk,
            'name': node.name,
            'code': node.code,
            'level': node.level,
            'parent': node.parent_id
        }
        children = [self.recursive_node_to_dict(c) for c in node.get_children()]
        if children:
            result['children'] = children
        return result


class ProductApplicabilitiesList(APIView):
    """Применимости продуктов"""

    def get (self, request):
        root_nodes = cache_tree_children(ProductApplicabilities.objects.all())
        dicts = []
        for n in root_nodes:
            dicts.append(self.recursive_node_to_dict(n))
        return Response(dicts)

    def recursive_node_to_dict(self, node):
        result = {
            'id': node.pk,
            'name': node.name,
            'code': node.code,
            'level': node.level,
            'parent': node.parent_id
        }
        children = [self.recursive_node_to_dict(c) for c in node.get_children()]
        if children:
            result['children'] = children
        return result


class ProductApplicabilitiesDetail(APIView):

    def get(self, request):
        id = request.GET['id']
        try:
            nodes = ProductApplicabilities.objects.get(pk=id)
        except ProductApplicabilities.DoesNotExist:
            return HttpResponse(status=201)

        if request.method == 'GET':
            dicts = []
            dicts.append(self.recursive_node_to_dict(nodes))
            return Response(dicts)

    def recursive_node_to_dict(self, node):
        result = {
            'id': node.pk,
            'name': node.name,
            'description': node.description,
            'code': node.code,
            'level': node.level,
            'parent': node.parent_id
        }
        children = [self.recursive_node_to_dict(c) for c in node.get_children()]
        if children:
            result['children'] = children
        return result





"""
==================== PAGES ======================
"""

def help(request):
    """Страничка хелпы по апи
    http://127.0.0.1:8000/api/v1/help
    """
    return render(request, 'help.html')