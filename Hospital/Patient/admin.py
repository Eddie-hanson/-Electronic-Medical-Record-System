from django.contrib import admin
from .models import RegisterPatient,PatientEncouter,PatientVitals,Nurse
# Register your models here.
admin.site.register(RegisterPatient)
admin.site.register(PatientEncouter)
admin.site.register(PatientVitals)
admin.site.register(Nurse)
