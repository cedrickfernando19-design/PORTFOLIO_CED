from rest_framework.serializers import ModelSerializer
from .models import Project, Certificate

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
