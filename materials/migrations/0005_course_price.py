# Generated by Django 4.2.9 on 2024-05-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0004_lesson_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="price",
            field=models.PositiveIntegerField(
                default="10000", verbose_name="Цена курса"
            ),
        ),
    ]