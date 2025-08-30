from django.db import models

# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=20)
    campus = models.ForeignKey("campus.Campus", on_delete=models.CASCADE)

class ExamResult(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey("classes.Subject", on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()
