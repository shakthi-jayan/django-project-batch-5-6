from django.urls import path
from .views import *

urlpatterns = [
    path("students/", student_list, name="student_list"),
    path("students/create", create_student, name="create_student")
]