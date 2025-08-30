from rest_framework import viewsets
from .models import Teacher, TeacherEducation, TeacherExperience, TeacherSummary
from .serializers import (
    TeacherSerializer,
    TeacherEducationSerializer,
    TeacherExperienceSerializer,
    TeacherSummarySerializer
)

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by("-created_at")
    serializer_class = TeacherSerializer


class TeacherEducationViewSet(viewsets.ModelViewSet):
    queryset = TeacherEducation.objects.all()
    serializer_class = TeacherEducationSerializer


class TeacherExperienceViewSet(viewsets.ModelViewSet):
    queryset = TeacherExperience.objects.all()
    serializer_class = TeacherExperienceSerializer


class TeacherSummaryViewSet(viewsets.ModelViewSet):
    queryset = TeacherSummary.objects.all()
    serializer_class = TeacherSummarySerializer
