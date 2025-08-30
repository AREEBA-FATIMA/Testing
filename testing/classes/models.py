from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

class ClassSection(models.Model):
    grade = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    campus = models.ForeignKey("campus.Campus", on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    teachers = models.ManyToManyField("teachers.Teacher", blank=True)
