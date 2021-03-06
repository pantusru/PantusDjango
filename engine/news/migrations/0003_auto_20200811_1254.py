# Generated by Django 3.0.8 on 2020-08-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200811_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_text_preview',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
