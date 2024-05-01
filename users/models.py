from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    avatar = models.ImageField(upload_to="users/", verbose_name="Аватар", **NULLABLE)
    phone_number = models.CharField(max_length=35, verbose_name="Номер телефона", **NULLABLE)
    city = models.CharField(max_length=150, verbose_name="Город", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    """Модель платежа"""
    class PaymentType(models.TextChoices):
        CASH = 'cash', 'наличные'
        SPENDING = 'spend', 'перевод на счет'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user', verbose_name='Пользователь', **NULLABLE)
    date = models.DateField(auto_now=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Сумма оплаты')
    payment_type = models.CharField(max_length=32, choices=PaymentType.choices, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('user', 'date')
