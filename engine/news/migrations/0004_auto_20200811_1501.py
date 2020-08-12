# Generated by Django 3.0.8 on 2020-08-11 11:01

from django.db import migrations
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200811_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_text_preview',
            field=news.models.TruncatingCharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=news.models.TruncatingCharField(max_length=255),
        ),
    ]
