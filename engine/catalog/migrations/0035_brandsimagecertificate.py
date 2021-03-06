# Generated by Django 3.0.8 on 2020-08-21 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0034_delete_brandsimagesсertificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandsImageCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images_certificate', to='catalog.Brands')),
            ],
            options={
                'verbose_name': 'Изображение сертификат',
                'verbose_name_plural': 'Изображение сертификат',
            },
        ),
    ]
