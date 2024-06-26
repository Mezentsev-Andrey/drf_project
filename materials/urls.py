from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseDetailView, CourseViewSet,
                             LessonCreateAPIView, LessonDestroyAPIView,
                             LessonListAPIView, LessonRetrieveAPIView,
                             LessonUpdateAPIView, SubscriptionCreateAPIView,
                             SubscriptionListAPIView)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/update/<int:pk>", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path(
        "lesson/detail/<int:pk>", LessonRetrieveAPIView.as_view(), name="lesson_detail"
    ),
    path(
        "lesson/delete/<int:pk>", LessonDestroyAPIView.as_view(), name="lesson_destroy"
    ),
    path(
        "subscription/create",
        SubscriptionCreateAPIView.as_view(),
        name="create_subscription",
    ),
    path("subscriptions/", SubscriptionListAPIView.as_view(), name="all_subscriptions"),
] + router.urls
