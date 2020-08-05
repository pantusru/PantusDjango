from urllib.error import HTTPError, URLError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
import urllib.request, json
from django.contrib import messages


# Create your views here.

# декоратор проверка авторизации
from ..models import PopularProduct


@login_required(login_url='/admin/')
def create_new_product(request):

    # проверка редиректа
    if request.META.get('HTTP_REFERER') is None:
        print('NO REDIRECT')
    else:
        # проверка http
        try:
                with urllib.request.urlopen("https://www.pantus.ru/api/rest/2.0/popular/") as url:
                    data = json.loads(url.read().decode())
        except HTTPError as e:
                print('Error code: ', e.code)
                # Then, when you need to error the user:
                messages.error(request, ('Error code: ', e.code))
        except URLError as e:
                print('Reason: ', e.reason)
                # Then, when you need to error the user:
                messages.error(request, ('Reason: ', e.reason))
        else:
            # запись в БД
            #print(data)
            #PopularProduct.objects.create(product_id="Tom", product_img=23)
            # parsed_string = json.dumps(data)
            # d2 = json.loads(parsed_string)

#для тестирования не удалять начало
            # print('==============================================================================')
            # print(id['id'])
            # print(id['name'])
            # print(id['images']['main'])
            # print(id['manufacturer']['name'])
            # print(id['sku'])
            # print(','.join(str(id['oem']['list']).split(',')[:3]) + ']')
            # print(id['offer']['prices']['retail'])
            # print(id['offer']['quantity'])
            # print('==============================================================================')
# для тестирования не удалять конец
            # product_oem обрезаем до макс. 3х значений оем
            for id in data['data']:


                PopularProduct.objects.create(
                    product_id=id['id'],
                    product_name = id['name'],
                    product_img = id['images']['main'],
                    product_manufacture = id['manufacturer']['name'],
                    product_articul = id['sku'],
                    product_oem = (','.join(str(id['oem']['list']).split(',')[:3]) + ']'),
                    product_price = id['offer']['prices']['retail'],
                    product_quantity = id['offer']['quantity'],
                )

            messages.success(request, "Импорт завершен")


        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # redirect back
