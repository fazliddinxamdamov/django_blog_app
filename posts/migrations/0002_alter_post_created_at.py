# Generated by Django 4.0.5 on 2022-06-07 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 7, 22, 50, 29, 534956)),
        ),
    ]
