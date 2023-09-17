from django.forms import ModelForm, modelformset_factory
from .models import *

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name',)

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('courses', 'name', 'lastname')

StudentFormSet = modelformset_factory(Student, form=StudentForm, extra=2)
