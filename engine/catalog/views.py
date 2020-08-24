from django.db import connection
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from .models import *

import urllib
import os
from urllib.error import HTTPError, URLError
from django.contrib import messages
import urllib.request, json
from django.http import HttpResponseRedirect, HttpResponse
#from ..models import *
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse
import urllib.request, json
from urllib.request import urlretrieve

# Create your views here.


def getiing(request):



    # queryset = Product.objects.filter(category__in=ProductCategory.objects.get(id=456).get_descendants(include_self=True))\
    #           # | Product.objects.filter(category__in=ProductCategory.objects.get(id=454).get_descendants(include_self=True))

    query = Q(category__in=ProductCategory.objects.get(id=456).get_descendants(include_self=True))
    #query.add(Q(category__in=ProductCategory.objects.get(id=454).get_descendants(include_self=True)), Q.OR)


    queryset = Product.objects.filter(query)

    print(queryset)
    print(connection.queries)


class BrandsView(View):


    def get(self, request):
        #return render(request, self.template_name, {})
        template_name = 'admin/catalog/Brands/page.html'
        data = DbApi().get_data('https://pantus.ru/api/rest/2.0/brands')
        print(data['data'])

        return render(request, template_name, {'d': data['data']},  content_type="text/html")

    def post(self, request):
      # Do something
      pass


class DbApi():

    def get_data(self, urlapi):
            try:
                with urllib.request.urlopen(urlapi) as url:
                    data = json.loads(url.read().decode())
            except HTTPError as e:
                print('Error code: ', e.code)
            except URLError as e:
                print('Reason: ', e.reason)
            else:
                return data
