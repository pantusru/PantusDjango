# Generated by Django 3.0.8 on 2020-08-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlcore', '0019_auto_20200805_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id', 'title'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]