from django.contrib.auth.models import User
from django.db import models
from apps.courses.models import CourseClass


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE, related_name="enrollments")
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["course_class__weekday", "course_class__start_period"]
        constraints = [
            models.UniqueConstraint(fields=["student", "course_class"], name="unique_student_course_class")
        ]

    def __str__(self):
        return f"{self.student.username} - {self.course_class.code}"
