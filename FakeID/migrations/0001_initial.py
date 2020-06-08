# Generated by Django 3.0.7 on 2020-06-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonymousID', models.CharField(max_length=100, verbose_name='Token')),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': 'IDs',
                'verbose_name_plural': 'IDs',
                'db_table': 'fakeid_user',
            },
        ),
    ]