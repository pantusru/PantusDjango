
from .models import *
# Create your views here.


def getiing(request):

    #print(ProductCategory.objects.get(id=2).get_descendants(include_self=True)) # от корневой к дочерним

    print(Product.objects.filter(category__in=ProductCategory.objects.get(id=5).get_descendants(include_self=True)))

