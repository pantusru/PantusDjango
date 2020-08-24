import shutil
import urllib
import os
from pathlib import Path

from django.conf import settings
import urllib.request
from urllib.parse import urlparse
import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as BS

class RestructUploadFile():
    """перекидываем файлы
            в свою структуру, изменяем ссылки на новые"""

    def file_move(self, soup, url_path_dir):

        media_root = settings.MEDIA_ROOT
        media_root = media_root.replace("\\", '/')
        soup = BS(soup)

        try:
            server_path_dir = media_root+url_path_dir

            for imgtag in soup.find_all('img'):
                full_url = urlparse(imgtag['src'])
                if full_url is not None:
                    file_name = os.path.basename(full_url.path)
                    download_url = (media_root + '/temp_editor/' + file_name)

                    if os.path.exists(download_url):
                        #если файл есть в temp_editor
                        os.makedirs(server_path_dir, exist_ok=True) #создаем для файла на сервере директорию если её нет
                        local_path_dir_new = server_path_dir.replace('/', '\\')
                        local_path_dir_temp = download_url.replace('/', '\\')
                        shutil.move(local_path_dir_temp, local_path_dir_new + '\\' + file_name)  # перемещаем файл
                        ######## ПОДМЕНА ТЕЛА ########
                        imgtag['src'] = '/media' + url_path_dir + '/' + file_name
                        ######## ПОДМЕНА ТЕЛА КОНЕЦ ########

            return str(soup)

        except:
            print("===================================== except ==========================================")
            return str(soup)

    def files_migrations(self, server_path_dir, download_url):  # разбить потом по методам
        pass


class RemoveFilesOnObject():

    def delete(self, url_path_dir):
        media_root = settings.MEDIA_ROOT
        server_path_dir = media_root + url_path_dir
        dirpath = Path(server_path_dir)
        if dirpath.exists() and dirpath.is_dir():
            shutil.rmtree(dirpath)