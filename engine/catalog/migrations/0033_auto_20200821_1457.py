# Generated by Django 3.0.8 on 2020-08-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_brands_brandsimagesphoto_brandsimagesсertificate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brands',
            options={'ordering': ['-id', 'name'], 'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='brandsimagesphoto',
            options={'verbose_name': 'Изображения фото', 'verbose_name_plural': 'Изображения фото'},
        ),
        migrations.AlterModelOptions(
            name='brandsimagesсertificate',
            options={'verbose_name': 'Изображение сертификат', 'verbose_name_plural': 'Изображение сертификат'},
        ),
        migrations.AlterField(
            model_name='brands',
            name='image_logo',
            field=models.ImageField(upload_to=''),
        ),
    ]