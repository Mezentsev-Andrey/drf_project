from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Модель учебного курса"""

    name = models.CharField(max_length=200, verbose_name="Название")
    preview = models.ImageField(upload_to="course_preview", verbose_name="Изображение", **NULLABLE)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель урока"""

    course = models.ForeignKey(Course, verbose_name="Курс", related_name="lesson", on_delete=models.SET_NULL,**NULLABLE)
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to="lesson_preview",verbose_name="Изображение",**NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
