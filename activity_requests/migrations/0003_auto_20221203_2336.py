# Generated by Django 3.0.1 on 2022-12-03 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_requests', '0002_auto_20221203_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='requet_user',
            new_name='request_user',
        ),
    ]
