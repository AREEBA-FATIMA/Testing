from django.db import models

# Create your models here.
class Attendance(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=(("present","Present"),("absent","Absent")))
