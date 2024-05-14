from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings
from config.settings import PAYMENT_METHOD_CHOICES
from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    avatar = models.ImageField(upload_to="users/", verbose_name="Аватар", **NULLABLE)
    phone_number = models.CharField(
        max_length=35, verbose_name="Номер телефона", **NULLABLE
    )
    city = models.CharField(max_length=150, verbose_name="Город", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    """Модель платежа"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="Пользователь",
        **NULLABLE,
    )
    payment_date = models.DateField(
        auto_now=True, verbose_name="Дата оплаты", **NULLABLE
    )
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE
    )
    payment_amount = models.PositiveIntegerField(
        verbose_name="Сумма оплаты", **NULLABLE
    )
    payment_type = models.CharField(
        max_length=50,
        choices=PAYMENT_METHOD_CHOICES,
        verbose_name="Способ оплаты",
        **NULLABLE,
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name="id сессии",
        **NULLABLE,
    )
    link = models.URLField(
        max_length=400,
        verbose_name="Cсылка на оплату",
        **NULLABLE,
    )

    def __str__(self) -> str:
        return f"{self.user}, {self.paid_course}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
