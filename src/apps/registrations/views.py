from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.courses.models import CourseClass
from .models import Enrollment
from .services import RegistrationError, cancel_registration, register_course


@login_required
def course_list(request):
    classes = CourseClass.objects.select_related("course").all()
    enrolled_ids = set(
        Enrollment.objects.filter(student=request.user).values_list("course_class_id", flat=True)
    )
    return render(request, "student/register_courses.html", {
        "classes": classes,
        "enrolled_ids": enrolled_ids,
    })


@login_required
@require_POST
def register(request, course_class_id):
    course_class = get_object_or_404(CourseClass.objects.select_related("course"), pk=course_class_id)
    try:
        register_course(request.user, course_class)
        messages.success(request, f"Đăng ký {course_class.code} thành công.")
    except RegistrationError as error:
        messages.error(request, str(error))
    return redirect("registrations:course_list")


@login_required
@require_POST
def cancel(request, course_class_id):
    course_class = get_object_or_404(CourseClass, pk=course_class_id)
    try:
        cancel_registration(request.user, course_class)
        messages.success(request, f"Đã hủy lớp {course_class.code}.")
    except RegistrationError as error:
        messages.error(request, str(error))
    return redirect("registrations:schedule")


@login_required
def schedule(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related("course_class__course")
    return render(request, "student/schedule.html", {"enrollments": enrollments})
