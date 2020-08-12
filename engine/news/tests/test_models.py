from datetime import datetime

from django.test import TestCase
from pytils.translit import slugify

from ..models import News
from ..models import NewsCategory
from django.contrib.auth import get_user_model
User = get_user_model()


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        NewsCategory.objects.create(
            name='testcategory'
        )

        User.objects.create(
            username = 'xxx'
        )

        News.objects.create(
            title='ТЕСТ',
            image='"/media/news/2019/04/10/preview_news_id_186957.jpg"',
            body_text_preview='ТЕСТ',
            body='ТЕСТ',
            category=NewsCategory.objects.get(id=1),
            keywords='',
            author=User.objects.get(id=1),
            # 24.03.2017 07:35:17 datetime.strptime(data['data']['dates']['created'], '%d.%m.%Y %H:%M:%S')
            created_at=datetime.strptime('24.03.2017 07:35:17', '%d.%m.%Y %H:%M:%S'),
            #slug = 'TEST'
        )

    def setUp(self):
        pass

    def test_title_label(self):
        news = News.objects.get(id=1)
        title_label = news._meta.get_field('category').verbose_name
        self.assertEquals(title_label, 'Категория')

    def test_title_max_length(self):
        news = News.objects.get(id=1)
        max_length = news._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_body_text_preview_max_length(self):
        news = News.objects.get(id=1)
        max_length = news._meta.get_field('body_text_preview').max_length
        self.assertEquals(max_length, 200)

    def test_keywords_max_length(self):
        news = News.objects.get(id=1)
        max_length = news._meta.get_field('keywords').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        news = News.objects.get(id=1)
        expected_object_name = '%s' % (news.title)
        self.assertEquals(expected_object_name, str(news))


    def test_slug_generation(self):

        lol = News.objects.create(title='ТЕСТ', id=0)
        lol.keywords='asdasdasd'
        lol.is_available()
        lol.save()
        self.assertEqual(lol.slug, slugify('ТЕСТ'), 'Ошибка генерации или коррекнтности слага')