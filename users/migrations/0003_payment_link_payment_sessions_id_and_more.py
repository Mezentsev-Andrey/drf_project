# Generated by Django 4.2.9 on 2024-05-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_payment_payment_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="link",
            field=models.URLField(
                blank=True,
                help_text="Укажите ссылку на оплату",
                max_length=400,
                null=True,
                verbose_name="ссылка на оплату",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="sessions_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите id сессии",
                max_length=255,
                null=True,
                verbose_name="id сессии",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Укажите сумму оплаты",
                max_digits=8,
                verbose_name="Сумма оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_type",
            field=models.CharField(
                choices=[("cash", "наличные"), ("spend", "перевод на счет")],
                help_text="Выберите способ оплаты",
                max_length=32,
                verbose_name="Способ оплаты",
            ),
        ),
    ]
