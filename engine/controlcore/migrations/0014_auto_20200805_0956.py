# Generated by Django 3.0.8 on 2020-08-05 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlcore', '0013_auto_20200804_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='controlcore.NewsCategory', verbose_name='Категория'),
        ),
    ]