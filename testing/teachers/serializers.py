from rest_framework import serializers
from .models import Teacher, TeacherEducation, TeacherExperience, TeacherSummary


class TeacherEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherEducation
        fields = "__all__"


class TeacherExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherExperience
        fields = "__all__"


class TeacherSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSummary
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    educations = TeacherEducationSerializer(many=True, read_only=True)
    experiences = TeacherExperienceSerializer(many=True, read_only=True)
    summary = TeacherSummarySerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = "__all__"
