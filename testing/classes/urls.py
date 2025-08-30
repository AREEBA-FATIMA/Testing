from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, ClassSectionViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'class-sections', ClassSectionViewSet)

urlpatterns = router.urls
