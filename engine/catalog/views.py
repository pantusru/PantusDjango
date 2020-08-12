from .models import *
# Create your views here.

def getiing(request):
    print('sdfdssdfsdfsdfsdf')

    print(Test.objects.filter(parent__in=Genre.objects.get(id=1).get_descendants(include_self=True)))