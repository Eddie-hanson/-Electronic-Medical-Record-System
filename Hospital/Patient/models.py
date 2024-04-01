from django.db import models

# Create your models here.

#1.	The front-desk executive should be a to register patients
# who do not already exist (patient ID, Surname, Other names,
# Gender, Phone Number, Residential Address, Emergency Name, 
# Contact and Relationship with Patient)-create modules.

class RegisterPatient(models.Model): #Class for registering patients
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    patientID= models.IntegerField(unique=True)
    Surname=models.CharField(max_length=25)
    OtherNames=models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    PhoneNumber=models.CharField( max_length=20)
    ResidentialAddress= models.CharField( max_length=200)
    EmergencyName= models.CharField(max_length=100)
    EmergencyContact= models.CharField(max_length=20)
    RelationshipwithPatient=models.CharField(max_length=20)
    
    def __str__(self):
        return self.OtherNames
    
    
#2.	The front-desk should be able to start an encounter (visitation) 
# #for a patient (Patient ID, Date and Time, 
# Type of encounter (Emergency/OPD/Specialist Care]-check how    

class PatientEncounter(models.Model):
    ENCOUNTER_CHOICES=(('Emergency','Emergency'),
                       ('OPD','OPD'),
                       ('Specialist Care','Specialist Care'),
                    
                       )
    PatientName=models.ForeignKey(RegisterPatient, on_delete=models.CASCADE)
    patientID= models.IntegerField()
    Date=models.DateField(("Date"), auto_now=True, auto_now_add=False)
    Time=models.TimeField(("Time"), auto_now=True, auto_now_add=False)
    Encounter=models.CharField(max_length=20,choices= ENCOUNTER_CHOICES)
    Description=models.TextField()
    def __str__(self):
        return f'Name: {self.PatientName}'
    
#Nurse should be able to submit patient vitals (Blood pressure/Temperature/Pulse/SP02). -check how.  
class Nurse(models.Model):
    name = models.CharField(max_length=100)
    # Add other nurse-related fields if needed
    
    def __str__(self):
        return self.name

class PatientVitals(models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    blood_pressure = models.CharField(max_length=20)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)  # Assuming Celsius
    pulse = models.PositiveSmallIntegerField()  # Assuming pulse is an integer value
    spO2 = models.PositiveSmallIntegerField()   # Assuming SP02 is a percentage
    
    submission_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient_name}'s Vitals - {self.submission_date} by {self.nurse}"