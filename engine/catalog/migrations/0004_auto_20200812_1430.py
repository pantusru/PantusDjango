# Generated by Django 3.0.8 on 2020-08-12 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_genre_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='parent_id',
            new_name='parent',
        ),
    ]
