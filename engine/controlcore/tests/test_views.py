from datetime import datetime, date

from django.http import JsonResponse
from django.test import TestCase
from django.urls import reverse
from import_export.formats.base_formats import JSON
from rest_framework.utils import json

from siteapi import serializers
from siteapi.serializers import NewsListSerializer
from ..models import News
from ..models import NewsCategory
from django.contrib.auth import get_user_model
User = get_user_model()
from siteapi.views import NewsListView


class NewsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        NewsCategory.objects.create(
            name='testcategory'
        )

        User.objects.create(
            username = 'xxx'
        )

        # Create 13 authors for pagination tests
        News.objects.create(
            #id=author_num,
            title='ТЕСТ',
            image='"/media/news/2019/04/10/preview_news_id_186957.jpg"',
            body_text_preview='ТЕСТ',
            body='ТЕСТ',
            category=NewsCategory.objects.get(id=1),
            keywords='',
            author=User.objects.get(id=1),
            # 24.03.2017 07:35:17 datetime.strptime(data['data']['dates']['created'], '%d.%m.%Y %H:%M:%S')
            #created_at=datetime.strptime('24.03.2017 07:35:17', '%d.%m.%Y %H:%M:%S'),
            #slug = 'TEST %s'
        )



    def test_view_api_news_list_created_at(self):
        """Тест на корректность и формат даты в веб апи"""

        today = date.today()
        response = self.client.get('/api/v1/news/')
        result = json.loads(response.content)
        result_year = result['results'][0]['created_at'][0]['year']
        result_month = result['results'][0]['created_at'][0]['month']
        result_day = result['results'][0]['created_at'][0]['day']
        self.assertEqual(result_year, today.strftime("%Y"), "date incorrect")
        self.assertEqual(result_month, today.strftime("%m"),"date incorrect")
        self.assertEqual(result_day, today.strftime("%d"), "date incorrect")






