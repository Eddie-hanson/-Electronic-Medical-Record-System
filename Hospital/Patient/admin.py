from django.contrib import admin
from .models import RegisterPatient,PatientEncounter,PatientVitals,Nurse
# Register your models here.
admin.site.register(RegisterPatient)
admin.site.register(PatientEncounter)
admin.site.register(PatientVitals)
admin.site.register(Nurse)
