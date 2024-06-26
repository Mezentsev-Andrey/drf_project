# Generated by Django 4.2.9 on 2024-05-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_payment_amount_alter_payment_course_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={
                "ordering": ("user", "payment_date"),
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
            },
        ),
        migrations.RenameField(
            model_name="payment",
            old_name="course",
            new_name="paid_course",
        ),
        migrations.RenameField(
            model_name="payment",
            old_name="lesson",
            new_name="paid_lesson",
        ),
        migrations.RenameField(
            model_name="payment",
            old_name="amount",
            new_name="payment_amount",
        ),
        migrations.RenameField(
            model_name="payment",
            old_name="date",
            new_name="payment_date",
        ),
        migrations.AlterField(
            model_name="payment",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Cсылка на оплату"
            ),
        ),
    ]
