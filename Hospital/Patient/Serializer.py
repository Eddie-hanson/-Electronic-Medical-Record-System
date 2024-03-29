
from rest_framework import serializers
from .models import RegisterPatient

class RegisterPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterPatient
        fields='__all__'