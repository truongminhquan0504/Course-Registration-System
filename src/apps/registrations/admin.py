from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course_class", "registered_at")
    list_filter = ("course_class__semester",)
    search_fields = ("student__username", "course_class__code")
