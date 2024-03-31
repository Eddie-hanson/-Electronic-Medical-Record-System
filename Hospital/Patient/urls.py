from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientsList, name='Patient-list'),
    path('CreatePatient/', views.CreatePatient, name='Create-Patient'),
    path('listpatient/<int:pk>/', views.NewPatientDetail, name='Patient-Detail'),
    path('updatePatient/<int:pk>/', views.updatePatient, name='updatePatient'),
    
    
    path('Visitaion/', views.PatientEncounterlist, name='PatientEncounter'),
    path('Visitaion/CreateEncounter/', views.CreateEncounter, name='CreateEncounter'),
    path('Visitaion/PatientEncounterUpdate/<int:pk>/', views.PatientEncounterUpdate, name='PatientEncounterUpdate'),
    path('Visitaion/PatientEncounterDetail/<int:pk>/', views.PatientEncounterDetail, name='PatientEncounterDetail'),
    path('Visitation/DeletePatientEncounter/<int:pk>/', views.DeletePatientEncounter, name='DeletePatientEncounter'),

]
