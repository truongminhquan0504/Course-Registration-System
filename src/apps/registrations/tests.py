from django.contrib.auth.models import User
from django.test import TestCase
from apps.courses.models import Course, CourseClass
from .models import Enrollment
from .services import RegistrationError, register_course


class RegistrationServiceTests(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(username="student", password="testpass123")
        self.course_a = Course.objects.create(code="WEB101", name="Lập trình web")
        self.course_b = Course.objects.create(code="DB101", name="Cơ sở dữ liệu")
        self.class_a = CourseClass.objects.create(
            course=self.course_a, code="WEB101-01", lecturer="Nguyễn Văn A", room="A101",
            weekday=2, start_period=1, end_period=3, max_students=30,
        )
        self.class_b = CourseClass.objects.create(
            course=self.course_b, code="DB101-01", lecturer="Trần Văn B", room="A102",
            weekday=2, start_period=3, end_period=5, max_students=30,
        )

    def test_cannot_register_overlapping_schedule(self):
        register_course(self.student, self.class_a)
        with self.assertRaises(RegistrationError):
            register_course(self.student, self.class_b)

    def test_cannot_register_full_class(self):
        self.class_a.max_students = 0
        self.class_a.save(update_fields=["max_students"])
        with self.assertRaises(RegistrationError):
            register_course(self.student, self.class_a)
        self.assertEqual(Enrollment.objects.count(), 0)
