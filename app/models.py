from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)