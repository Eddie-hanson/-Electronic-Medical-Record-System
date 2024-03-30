from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .models import RegisterPatient,PatientEncouter,Nurse,PatientVitals
from .Serializer import RegisterPatientSerializer

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