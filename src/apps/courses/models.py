from django.db import models


class Course(models.Model):
    code = models.CharField("Mã môn", max_length=20, unique=True)
    name = models.CharField("Tên môn", max_length=150)
    credits = models.PositiveSmallIntegerField("Số tín chỉ", default=3)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class CourseClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="classes")
    code = models.CharField("Mã lớp học phần", max_length=30, unique=True)
    lecturer = models.CharField("Giảng viên", max_length=120)
    room = models.CharField("Phòng", max_length=30)
    weekday = models.PositiveSmallIntegerField("Thứ", choices=[(i, f"Thứ {i}") for i in range(2, 8)])
    start_period = models.PositiveSmallIntegerField("Tiết bắt đầu")
    end_period = models.PositiveSmallIntegerField("Tiết kết thúc")
    max_students = models.PositiveIntegerField("Sĩ số tối đa", default=50)
    semester = models.CharField("Học kỳ", max_length=30, default="2026-2027 HK1")

    class Meta:
        ordering = ["weekday", "start_period", "code"]

    def __str__(self):
        return f"{self.code} - {self.course.name}"
