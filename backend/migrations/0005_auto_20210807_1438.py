# Generated by Django 3.2.6 on 2021-08-07 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210807_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 14, 38, 12, 857814)),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 14, 38, 12, 941227)),
        ),
    ]
