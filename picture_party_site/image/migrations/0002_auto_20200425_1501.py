# Generated by Django 3.0.5 on 2020-04-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("image", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
