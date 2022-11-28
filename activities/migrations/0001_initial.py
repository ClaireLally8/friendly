# Generated by Django 4.1.3 on 2022-11-28 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('start_datetime', models.DateTimeField()),
                ('end_time', models.TimeField()),
                ('location', models.CharField(blank=True, choices=[('carlow', 'Carlow'), ('cavan', 'Cavan'), ('clare', 'Clare'), ('cork', 'Cork'), ('donegal', 'Donegal'), ('dublin', 'Dublin'), ('galway', 'Galway'), ('kerry', 'Kerry'), ('kildare', 'Kildare'), ('kilkenny', 'Kilkenny'), ('laois', 'Laois'), ('leitrim', 'Leitrim'), ('limerick', 'Limerick'), ('longford', 'Longford'), ('louth', 'Louth'), ('mayo', 'Mayo'), ('meath', 'Meath'), ('monaghan', 'Monaghan'), ('offaly', 'Offaly'), ('roscommon', 'Roscommon'), ('sligo', 'Sligo'), ('tipperary', 'Tipperary'), ('waterford', 'Waterford'), ('westmeath', 'Westmeath'), ('wexford', 'Wexford'), ('wicklow', 'Wicklow')], max_length=200, null=True)),
                ('town', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(max_length=140)),
                ('available', models.BooleanField(default=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
