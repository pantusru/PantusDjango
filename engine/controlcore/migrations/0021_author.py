# Generated by Django 3.0.8 on 2020-08-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlcore', '0020_auto_20200805_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
        ),
    ]