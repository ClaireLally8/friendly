# Generated by Django 3.0.1 on 2022-12-03 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_requests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='activity',
            new_name='request_activity',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='user',
            new_name='requet_user',
        ),
    ]
