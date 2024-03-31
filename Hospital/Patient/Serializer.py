
from rest_framework import serializers
from .models import RegisterPatient, PatientEncounter

class RegisterPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterPatient
        fields='__all__'
        
        
class PatientEncounterSerializer(serializers.ModelSerializer) :    
    class Meta:
        model=PatientEncounter
        fields='__all__'
        