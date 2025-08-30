from rest_framework import viewsets, decorators, response
from .models import Campus
from .serializers import CampusSerializer

class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer

    # ✅ Custom endpoint: campus summary
    @decorators.action(detail=True, methods=["get"])
    def summary(self, request, pk=None):
        campus = self.get_object()
        data = {
            "name": campus.name,
            "code": campus.code,
            "num_students": campus.num_students,
            "num_teachers": campus.num_teachers,
            "teacher_student_ratio": campus.teacher_student_ratio,
            "capacity": campus.capacity,
        }
        return response.Response(data)

    # ✅ Custom endpoint: facilities list
    @decorators.action(detail=True, methods=["get"])
    def facilities(self, request, pk=None):
        campus = self.get_object()
        data = {
            "science_labs": campus.science_labs,
            "computer_labs": campus.computer_labs,
            "library": campus.library,
            "toilets": {
                "male": campus.toilets_male,
                "female": campus.toilets_female,
                "accessible": campus.toilets_accessible,
            },
            "internet_wifi": campus.internet_wifi,
            "power_backup": campus.power_backup,
        }
        return response.Response(data)

    # ✅ Custom endpoint: only active campuses
    @decorators.action(detail=False, methods=["get"])
    def active(self, request):
        campuses = Campus.objects.filter(status="active")
        serializer = self.get_serializer(campuses, many=True)
        return response.Response(serializer.data)
