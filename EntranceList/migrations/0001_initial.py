# Generated by Django 3.0.7 on 2020-06-08 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Stores', '0006_auto_20200608_1518'),
        ('FakeID', '0004_auto_20200608_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntranceList',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('visit_dttm', models.DateTimeField(auto_now_add=True, verbose_name='입장 시간')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stores.Store', verbose_name='시설')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FakeID.ID', verbose_name='사용자')),
            ],
            options={
                'verbose_name': '입장 목록',
                'verbose_name_plural': '입장 목록',
                'db_table': 'EntranceList',
            },
        ),
    ]
