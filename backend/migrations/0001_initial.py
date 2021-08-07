# Generated by Django 3.1.7 on 2021-08-07 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('file_id', models.CharField(default='', max_length=1000, unique=True)),
                ('upload_at', models.DateTimeField(default=datetime.datetime(2021, 8, 7, 18, 59, 12, 446157))),
                ('lock', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=2)),
                ('delete_file', models.CharField(choices=[('Normal', 'Normal'), ('deleted', 'deleted')], default='Normal', max_length=10)),
                ('password', models.CharField(default='none', max_length=100)),
                ('name', models.CharField(max_length=1000)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('like_on', models.DateTimeField(default=datetime.datetime(2021, 8, 7, 18, 59, 12, 482564))),
                ('name', models.CharField(default='Unknown', max_length=1000)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('likeno', models.CharField(default='1', max_length=10000)),
            ],
        ),
    ]
