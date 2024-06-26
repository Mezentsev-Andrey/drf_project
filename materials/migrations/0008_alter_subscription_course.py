# Generated by Django 4.2.9 on 2024-05-20 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0007_alter_lesson_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course_for_subscription",
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]
