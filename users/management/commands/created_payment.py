import datetime

from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)

        self.payment1 = None
        self.payment2 = None
        self.payment3 = None
        self.payment4 = None

    def handle(self, *args, **kwargs):
        Payment.objects.all().delete()

        user1, created = User.objects.get_or_create(email="user1@test.ru")
        user2, created = User.objects.get_or_create(email="user2@test.ru")

        course1, created = Course.objects.get_or_create(name="Курс 1")
        course2, created = Course.objects.get_or_create(name="Курс 2")

        lesson1, created = Lesson.objects.get_or_create(name="Урок 1")
        lesson2, created = Lesson.objects.get_or_create(name="Урок 2")

        self.payment1 = Payment.objects.create(
            user=user1,
            date=datetime.datetime.now().date,
            course=course1,
            amount=170,
            payment_type="cash",
        )

        self.payment2 = Payment.objects.create(
            user=user2,
            date=datetime.datetime.now().date,
            course=course2,
            amount=356,
            payment_type="spend",
        )

        self.payment3 = Payment.objects.create(
            user=user1,
            date=datetime.datetime.now().date,
            course=course2,
            lesson=lesson1,
            amount=789,
            payment_type="cash",
        )

        self.payment4 = Payment.objects.create(
            user=user2,
            date=datetime.datetime.now().date,
            course=course1,
            lesson=lesson2,
            amount=834,
            payment_type="spend",
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Процесс тестирования завершен. Платежные данные загружены."
            )
        )
