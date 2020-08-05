from django.http import JsonResponse
from django.core import serializers
from ..models import News


def get_news(request):



    snippets1 = News.objects.all()

    data2 = serializers.serialize("json", snippets1)

    print(str(data2).encode('utf-8'))
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data2, safe=False, json_dumps_params={'ensure_ascii': False})
