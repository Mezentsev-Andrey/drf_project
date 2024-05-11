from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="admin@admin.com",
            is_superuser=True,
            is_staff=True,
        )
        self.user.set_password("1234")
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(
            name="New lesson",
            description="New lesson description",
            video="youtube.com/watch/000",
            owner=self.user,
        )

    def test_lesson_retrieve(self):
        """Test for getting list of lessons"""

        response = self.client.get(
            reverse("materials:lesson_detail", args=(self.lesson.pk,))
        )
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_create_lesson(self):
        """Тест создания урока"""
        data = {"name": "New lesson", "description": "New lesson description"}
        url = reverse("materials:lesson_create")
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_list_lesson(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "preview": None,
                    "video": "youtube.com/watch/000",
                    "course": None,
                    "owner": self.user.pk,
                },
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK),

        self.assertEqual(data, result)

    #
    def test_update_lesson(self):
        """Тест обновления урока"""

        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            "name": "Good lesson",
        }
        response = self.client.patch(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Good lesson")

    def test_delete_lesson(self):
        """Тест удаления урока"""

        url = reverse("materials:lesson_destroy", args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="admin@admin.com",
            is_superuser=True,
            is_staff=True,
        )
        self.course = Course.objects.create(
            name="Test Course", description="This is a test course"
        )
        self.client.force_authenticate(user=self.user)
        self.lesson = Lesson.objects.create(
            name="New lesson",
            description="New lesson description",
            video="youtube.com/watch/000",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        """Тест на получение курса"""

        url = reverse("materials:course_detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False,
        )
        self.user.set_password("1234")
        self.user.save()

        self.course = Course.objects.create(
            name="Course 1", description="Course name testing", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        """Тест на добавление подписки"""

        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        url = reverse("materials:subscription")
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "подписка добавлена")
