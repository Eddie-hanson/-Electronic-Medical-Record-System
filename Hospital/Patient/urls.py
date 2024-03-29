from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientsList, name='Patient-list'),
    path('CreatePatient/', views.CreatePatient, name='Create-Patient'),
   
    path('listpatient/<int:pk>/', views.NewPatientDetail, name='Patient-Detail'),
    path('updatePatient/<int:pk>/', views.updatePatient, name='updatePatient')

]
