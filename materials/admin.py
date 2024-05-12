from django.contrib import admin

from materials.models import Course, CourseSubscription, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview")
    search_fields = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview", "course", "video")
    search_fields = ("name", "course")


@admin.register(CourseSubscription)
class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "course")
    search_fields = ("user",)
