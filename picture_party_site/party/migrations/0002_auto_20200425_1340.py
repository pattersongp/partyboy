# Generated by Django 3.0.5 on 2020-04-25 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("party", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="party",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 4, 25, 13, 40, 54, 482389),
                verbose_name="date published",
            ),
        ),
    ]
