# Generated by Django 3.0.8 on 2020-08-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_text_preview',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=2000),
        ),
    ]
