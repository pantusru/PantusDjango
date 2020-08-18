from django.db import connection
from django.db.models import Q

from .models import *
# Create your views here.


def getiing(request):



    # queryset = Product.objects.filter(category__in=ProductCategory.objects.get(id=456).get_descendants(include_self=True))\
    #           # | Product.objects.filter(category__in=ProductCategory.objects.get(id=454).get_descendants(include_self=True))

    query = Q(category__in=ProductCategory.objects.get(id=456).get_descendants(include_self=True))
    #query.add(Q(category__in=ProductCategory.objects.get(id=454).get_descendants(include_self=True)), Q.OR)


    queryset = Product.objects.filter(query)

    print(queryset)
    print(connection.queries)

