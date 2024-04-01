from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .models import RegisterPatient,PatientEncounter,Nurse,PatientVitals
from .Serializer import RegisterPatientSerializer, PatientEncounterSerializer,PatientVitalsSerializer
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def CreatePatient(request):
    
    serializer1=RegisterPatientSerializer(data=request.data)
    if serializer1.is_valid():
        serializer1.save()
        return Response(serializer1.data)
    return Response(serializer1.data)



def PatientsList(request):
   Patient=RegisterPatient.objects.all()
   serializer1=RegisterPatientSerializer(Patient, many = True)
   return JsonResponse(serializer1.data, safe= False)

@api_view(['GET'])
def NewPatientDetail(request, pk):
   try:
       Patient=RegisterPatient.objects.get(id=pk)
   except RegisterPatient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)    
   serializer1=RegisterPatientSerializer(Patient)
   return JsonResponse(serializer1.data, safe= False, )

@api_view(['PUT'])
def updatePatient(request, pk):
    
   patient = RegisterPatient.objects.get(RegisterPatient, pk=pk)
    
   
   serializer1 = RegisterPatientSerializer(patient, data=request.data)
   if serializer1.is_valid():
        serializer1.save()
        return Response(serializer1.data)
    
    
   return Response(serializer1.errors, status=400)


def PatientEncounterlist(request): # to view all encounters
   Patient=PatientEncounter.objects.all()
   serializer2=PatientEncounterSerializer(Patient, many = True)
   return JsonResponse(serializer2.data, safe= False)

@api_view(['POST'])
def CreateEncounter(request):
   serializer2=PatientEncounterSerializer(data=request.data)
   if serializer2.is_valid():
      serializer2.save()
      
   return Response(serializer2.data)   

@api_view(['GET'])
def PatientEncounterDetail(request, pk):
   try:
      Patient=PatientEncounter.objects.get(id=pk)
   except PatientEncounter.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)    
   serializer2=PatientEncounterSerializer(Patient)
   return JsonResponse(serializer2.data, safe= False, )



@api_view(['PUT'])
def PatientEncounterUpdate(request, pk):
   patient = PatientEncounter.objects.get(PatientEncounter, pk=pk)
    
   
   serializer2 = PatientEncounterSerializer(patient, data=request.data)
   if serializer2.is_valid():
        serializer2.save()
        return Response(serializer2.data)
    
    
   return JsonResponse(serializer2.errors, status=400)

@api_view(['DELETE'])
def DeletePatientEncounter(request, pk):
   try:
      patient = PatientEncounter.objects.get(pk=pk)
   except PatientEncounter.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   patient.delete()
   return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def CreatePatientVitals(request):
   Serializer3=PatientVitalsSerializer(data=request.data)
   if Serializer3.is_valid():
      Serializer3.save()
   return Response(Serializer3.data)   

def ListPatientVitals(request):
   Vitals=PatientVitals.objects.all()
   Serializer3=PatientVitalsSerializer(Vitals,many=True)
   return JsonResponse(Serializer3.data, safe=False)

def PatientVitalsDetails(request,pk):
   try:
      Vitals=PatientVitals.object.get(pk=pk)
   except PatientVitals.DoesNotExist:
     return JsonResponse('No vitals to show for this patient')   
  
@api_view(['PUT'])
def PatientVitalsDetails(request, pk):
   Vitals=PatientVitals.objects.get(pk=pk)
   
   Serializer3=PatientVitalsSerializer(data=request.data)
   if Serializer3.is_valid():
      Serializer3.save()
   return Response(Serializer3.data)   
  
  
  






  