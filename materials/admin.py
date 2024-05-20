from django.contrib import admin

from materials.models import Course, Subscription, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview")
    search_fields = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview", "course", "video")
    search_fields = ("name", "course")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("subscriber", "course")
    search_fields = ("subscriber",)
