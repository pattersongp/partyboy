# Generated by Django 3.0.5 on 2020-04-25 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("party", "0005_auto_20200425_1636"),
    ]

    operations = [
        migrations.AlterField(
            model_name="party",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 4, 25, 16, 36, 16, 361203),
                verbose_name="date published",
            ),
        ),
    ]
