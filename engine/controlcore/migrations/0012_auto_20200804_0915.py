# Generated by Django 3.0.8 on 2020-08-04 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlcore', '0011_auto_20200731_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='controlcore.NewsCategory', verbose_name='Категория'),
        ),
    ]