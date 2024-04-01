
from rest_framework import serializers
from .models import RegisterPatient, PatientEncounter,PatientVitals

class RegisterPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterPatient
        fields='__all__'
        
        
class PatientEncounterSerializer(serializers.ModelSerializer) :   
    # nurse_name = serializers.CharField(source='nurse.name', read_only=True) 
    class Meta:
        model=PatientEncounter
        fields='__all__'
        
class PatientVitalsSerializer(serializers.ModelSerializer):
    NurseName = serializers.CharField(source='nurse.name', read_only=True)
    class Meta:
        model=PatientVitals
        # fields='__all__'     
        exclude = ['nurse']   
        #This line of code displays all the fields in the Patient vitals class but Excludes nurse ID (Default Nurse ID) and  NurseName 