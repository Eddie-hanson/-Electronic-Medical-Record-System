from django.urls import path
from . import views

urlpatterns = [
    path('Register/', views.PatientsList, name='Patient-list'),
    path('Register/CreatePatient/', views.CreatePatient, name='Create-Patient'),
    path('Register/listpatient/<int:pk>/', views.NewPatientDetail, name='Patient-Detail'),
    path('Register/updatePatient/<int:pk>/', views.updatePatient, name='updatePatient'),
    
    
    path('Visitaion/', views.PatientEncounterlist, name='PatientEncounter'),
    path('Visitaion/CreateEncounter/', views.CreateEncounter, name='CreateEncounter'),
    path('Visitaion/PatientEncounterUpdate/<int:pk>/', views.PatientEncounterUpdate, name='PatientEncounterUpdate'),
    path('Visitaion/PatientEncounterDetail/<int:pk>/', views.PatientEncounterDetail, name='PatientEncounterDetail'),
    path('Visitation/DeletePatientEncounter/<int:pk>/', views.DeletePatientEncounter, name='DeletePatientEncounter'),
    
    
    path('Vitals/',views.ListPatientVitals, name='ListPatientVitals'),
    path('Vitals/CreatePatientVitals/',views.CreatePatientVitals, name='CreatePatientVitals'),
    path('Vitals/PatientVitalsDetails/<int:pk>/', views.PatientVitalsDetails, name='PatientVitalsDetails'),
    path('Vitals/PatientVitalsDetails/<int:pk>/', views.PatientVitalsDetails, name='PatientVitalsDetails')
    

]
