# Generated by Django 3.1.4 on 2020-12-27 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20201227_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='opinions',
            new_name='opinionss',
        ),
    ]
