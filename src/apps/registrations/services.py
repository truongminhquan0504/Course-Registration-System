from django.db import transaction
from .models import Enrollment


class RegistrationError(Exception):
    """Lỗi nghiệp vụ khi đăng ký học phần không hợp lệ."""


def _has_schedule_conflict(new_class, current_classes):
    for current_class in current_classes:
        same_day = current_class.weekday == new_class.weekday
        overlaps = (
            new_class.start_period <= current_class.end_period
            and current_class.start_period <= new_class.end_period
        )
        if same_day and overlaps:
            return current_class
    return None


@transaction.atomic
def register_course(student, course_class):
    if Enrollment.objects.filter(student=student, course_class=course_class).exists():
        raise RegistrationError("Bạn đã đăng ký lớp học phần này.")

    registered_count = Enrollment.objects.filter(course_class=course_class).count()
    if registered_count >= course_class.max_students:
        raise RegistrationError("Lớp học phần đã đủ sĩ số.")

    current_classes = [
        enrollment.course_class
        for enrollment in Enrollment.objects.select_related("course_class").filter(student=student)
    ]
    conflict = _has_schedule_conflict(course_class, current_classes)
    if conflict:
        raise RegistrationError(
            f"Trùng lịch với lớp {conflict.code} ({conflict.course.name})."
        )

    return Enrollment.objects.create(student=student, course_class=course_class)


def cancel_registration(student, course_class):
    deleted_count, _ = Enrollment.objects.filter(
        student=student, course_class=course_class
    ).delete()
    if deleted_count == 0:
        raise RegistrationError("Bạn chưa đăng ký lớp học phần này.")
