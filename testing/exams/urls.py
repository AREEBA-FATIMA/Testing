from rest_framework.routers import DefaultRouter
from .views import ExamViewSet, ExamResultViewSet

router = DefaultRouter()
router.register(r'exams', ExamViewSet)
router.register(r'exam-results', ExamResultViewSet)

urlpatterns = router.urls
