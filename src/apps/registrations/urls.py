from django.urls import path
from . import views

app_name = "registrations"

urlpatterns = [
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:course_class_id>/register/", views.register, name="register"),
    path("courses/<int:course_class_id>/cancel/", views.cancel, name="cancel"),
    path("schedule/", views.schedule, name="schedule"),
]
