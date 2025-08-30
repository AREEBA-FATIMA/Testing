from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeacherViewSet,
    TeacherEducationViewSet,
    TeacherExperienceViewSet,
    TeacherSummaryViewSet
)

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'teacher-educations', TeacherEducationViewSet, basename='teacher-education')
router.register(r'teacher-experiences', TeacherExperienceViewSet, basename='teacher-experience')
router.register(r'teacher-summaries', TeacherSummaryViewSet, basename='teacher-summary')

urlpatterns = [
    path("", include(router.urls)),
]
