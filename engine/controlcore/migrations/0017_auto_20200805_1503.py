# Generated by Django 3.0.8 on 2020-08-05 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlcore', '0016_auto_20200805_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
