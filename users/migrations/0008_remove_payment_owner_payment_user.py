# Generated by Django 4.2.9 on 2024-05-13 20:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_payment_options_remove_payment_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="owner",
        ),
        migrations.AddField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]