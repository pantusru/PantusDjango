import urllib
import os
from urllib.error import HTTPError, URLError
from django.contrib import messages
import urllib.request, json
from django.http import HttpResponseRedirect
from ..models import *
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse
import urllib.request, json
from urllib.request import urlretrieve


class ImportProductApplicabilities():
    pass

    def insert_table_catalog_productapplicabilities(self, request):

        # проверка редиректа
        if request.META.get('HTTP_REFERER') is None:
            print('NO REDIRECT')
        else:
            # проверка http
            try:
                with urllib.request.urlopen("https://pantus.ru/api/rest/2.0/applicabilities") as url:
                    data = json.loads(url.read().decode())
            except HTTPError as e:
                print('Error code: ', e.code)
                messages.error(request, ('Error code: ', e.code))
            except URLError as e:
                print('Reason: ', e.reason)
                messages.error(request, ('Reason: ', e.reason))
            else:

                pass
                # запись в БД

                for id in data['data']:

                    print(id)

                    description_html = id['description']
                    id_url_folder = id['id']
                    soup = BS(description_html)
                    # C:\PantusDjango\engine\media\product\applicabilities
                    path_dir = f'C://PantusDjango/engine/media/product/applicabilities/{id_url_folder}'
                    new_path_dir = f'/media/product/applicabilities/{id_url_folder}'

                    update_description = self.update_url_img_in_text_body(soup, path_dir, new_path_dir)  # html с обновлёными картинками



                    ProductApplicabilities.objects.create(
                        id=id['id'],
                        name=id['name'],
                        code=id['code'],
                        parent_id=id['parentId'],
                        description=update_description,
                    )

                print('======= END =========')
                messages.success(request, "Импорт завершен")

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # redirect back


    def update_url_img_in_text_body(self, soup, path_dir, new_path_dir):
        """Скачиваем и меняет урлы картинок в html"""

        try:
            path_dir = path_dir
            new_path_dir = new_path_dir

            for imgtag in soup.find_all('img'):

                full_url = urlparse(imgtag['src'])
                if full_url is not None:
                    file_name = os.path.basename(full_url.path)
                    download_url = 'http://www.pantus.ru' + urllib.parse.quote(imgtag['src'])
                    # print('====================== '+s)

                    os.makedirs(path_dir, exist_ok=True)
                    urlretrieve(download_url, path_dir + '/' + file_name)

                    ######## ПОДМЕНА ТЕЛА ########
                    imgtag['src'] = new_path_dir + '/' + file_name
            return str(soup)
            ######## ПОДМЕНА ТЕЛА КОНЕЦ ########

        except:
            print("===================================== except ==========================================")
            return str(soup)

