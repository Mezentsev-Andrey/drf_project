from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """Модель учебного курса"""

    name = models.CharField(max_length=200, verbose_name="Название")
    preview = models.ImageField(
        upload_to="course_preview", verbose_name="Изображение", **NULLABLE
    )
    description = models.TextField(verbose_name="Описание")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец",
    )
    price = models.PositiveIntegerField(default="10000", verbose_name="Цена курса")

    def __str__(self):
        return f"{self.name}, {self.price}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель урока"""

    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(
        upload_to="lesson_preview", verbose_name="Изображение", **NULLABLE
    )
    video = models.CharField(max_length=300, verbose_name="Ссылка на видео", **NULLABLE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    """Модель подписки на курс"""

    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Подписчик",
        **NULLABLE,
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    is_active = models.BooleanField(default=False, verbose_name="Активна")

    class Meta:
        verbose_name = "Подписка на курс"
        verbose_name_plural = "Подписки на курс"

    def __str__(self):
        return f"{self.course} {self.subscriber}"
