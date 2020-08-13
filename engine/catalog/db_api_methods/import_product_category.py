import urllib
from urllib.error import HTTPError, URLError

from django.contrib import messages
import urllib.request, json
from django.http import HttpResponseRedirect

from ..models import *





class ImportProductCategory():

    def insert_table_catalog_productcategory(self, request):

        # проверка редиректа
        if request.META.get('HTTP_REFERER') is None:
            print('NO REDIRECT')
        else:
            # проверка http
            try:
                with urllib.request.urlopen("https://www.pantus.ru/api/rest/2.0/categories/") as url:
                    data = json.loads(url.read().decode())
            except HTTPError as e:
                print('Error code: ', e.code)
                messages.error(request, ('Error code: ', e.code))
            except URLError as e:
                print('Reason: ', e.reason)
                messages.error(request, ('Reason: ', e.reason))
            else:
                # запись в БД

                for id in data['data']:

                    print(id)

                    ProductCategory.objects.create(
                        id=id['id'],
                        name=id['name'],
                        code=id['code'],
                        parent_id=id['parentId'],

                    )
                print('======= END =========')
                messages.success(request, "Импорт завершен")

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # redirect back







