# Generated by Django 3.0.5 on 2020-04-25 21:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("party", "0003_auto_20200425_1519"),
    ]

    operations = [
        migrations.AlterField(
            model_name="party",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 4, 25, 16, 35, 54, 881066),
                verbose_name="date published",
            ),
        ),
    ]
