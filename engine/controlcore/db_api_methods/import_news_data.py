import os
from datetime import datetime
from urllib.parse import urlparse
import urllib.request, json
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as BS

from controlcore.models import News
from controlcore.models import NewsCategory
from django.contrib.auth import get_user_model
User = get_user_model()


def importNewsData(request):

    my_list = []
    new_body = ''
    new_preview_img_url=''

    with urllib.request.urlopen("https://www.pantus.ru/api/rest/2.0/news/") as url:
        data = json.loads(url.read().decode())

        for id in data['data']:
            my_list.append(id)

        for id in my_list:

            urlgen=(f'https://www.pantus.ru/api/rest/2.0/news/{id}/')

            print(urlgen)
            try:
                with urllib.request.urlopen(urlgen) as url:
                    data = json.loads(url.read().decode())

                    ########## перенос изображений ################

                    news_year = datetime.strptime(data['data']['dates']['created'], '%d.%m.%Y %H:%M:%S').strftime("%Y")
                    news_month = datetime.strptime(data['data']['dates']['created'], '%d.%m.%Y %H:%M:%S').strftime("%m")
                    news_day = datetime.strptime(data['data']['dates']['created'], '%d.%m.%Y %H:%M:%S').strftime("%d")


                    # тут из Бади парсим
                    body_html=data['data']['content']

                    soup = BS(body_html)
                    for imgtag in soup.find_all('img'):

                        path_dir = f'C://PantusDjango/engine/media/news/{news_year}/{news_month}/{news_day}/body'
                        new_path_dir = f'/media/news/{news_year}/{news_month}/{news_day}/body'

                        full_url = urlparse(imgtag['src'])
                        if full_url is not None:
                            file_name = os.path.basename(full_url.path)
                            s='http://www.pantus.ru'+urllib.parse.quote(imgtag['src'])
                            #print('====================== '+s)

                            os.makedirs(path_dir, exist_ok=True)

                            urlretrieve(s, path_dir+'/'+file_name)

                            ######## ПОДМЕНА ТЕЛА ########

                            imgtag['src'] = new_path_dir+'/'+file_name
                            new_body = str(soup)

                            ######## ПОДМЕНА ТЕЛА КОНЕЦ ########



                    # Тут из джисона берем картинку

                    source_url = data['data']['preview']['image']

                    #print(new_body)


                    #print('SOURCE URL======= ', source_url)
                    if (source_url is not None):

                        print('source_url========= ' + source_url)
                        filename, file_extension = os.path.splitext(source_url)
                        path = urlparse(source_url).path
                        print('path========= ' + path)

                        full_url = source_url.replace('%20',' ')
                        query_string = urllib.parse.quote(full_url, safe=':/')

                        print('HEEEREEEEE ===== '+query_string)
                        path_dir=f'C://PantusDjango/engine/media/news/{news_year}/{news_month}/{news_day}'  # использовать от {news_year}
                        new_path_dir = f'news/{news_year}/{news_month}/{news_day}'  # использовать от {news_year}
                        os.makedirs(path_dir, exist_ok=True)

                        urlretrieve(query_string, path_dir+'/preview_news_id_'+str(id)+file_extension)
                        new_preview_img_url=new_path_dir+'/preview_news_id_'+str(id)+file_extension
                    ########## перенос изображений КОНЕЦ ################


                if data['data']['category']['id'] == 5297:
                    catid= 2
                elif data['data']['category']['id'] == 5298:
                    catid = 3
                elif data['data']['category']['id'] == 5299:
                    catid = 4
                elif data['data']['category']['id'] == 5296:
                    catid = 5
                elif data['data']['category']['id'] == 5294:
                    catid = 6
                elif data['data']['category']['id'] == 5295:
                    catid = 7
                elif data['data']['category']['id'] == 5292:
                    catid = 8
                else:
                    catid=None

                print("catid ", catid)

                News.objects.create(

                # id=44,
                    title=data['data']['name'],
                    image=new_preview_img_url,
                    body_text_preview=data['data']['preview']['text'],
                    body=new_body,

                    category=NewsCategory.objects.get(id=catid) if (catid is not None) else None,

                    keywords='',
                    author=User.objects.get(id=1),
                    # 24.03.2017 07:35:17 datetime.strptime(data['data']['dates']['created'], '%d.%m.%Y %H:%M:%S')
                    created_at=datetime.strptime(data['data']['dates']['created'], '%d.%m.%Y %H:%M:%S'),
                    # slug = 'null1'
                )

            except Exception as e:
                print('ERROR '+str(e))
                pass


