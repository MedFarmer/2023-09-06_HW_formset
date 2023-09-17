from django.urls import path
from .models import *
from .views import *
from django.views.generic import ListView
urlpatterns = [
    path('', ListView.as_view(template_name='courses.html', model=Course, context_object_name='courses'), name='list'),
    path('course/', CreateCourse.as_view(), name='course-create'),
    path('students/', CreateStudent.as_view(), name='students-create'),
    path('course/<int:pk>', CourseView.as_view(), name='course'),
    path('create_course/', create_course, name='create_course'),
]
