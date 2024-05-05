# Electronic Medical Record System
 This repository contains the backend implementation of an Electronic Medical Record (EMR) System. The system aims to streamline patient registration, encounter management, and vital submissions within a medical center.
 The EMR system is built using Django with Django Rest Framework for building RESTful APIs and PostgreSQL for data persistence.

## Functionalities Implemented:

### Patient Registration:

Allows the front-desk executive to register new patients who do not already exist in the system.

Endpoint: POST /api/Register/CreatePatient/


### Encounter Management:

Enables the front-desk to initiate an encounter (visitation) for a patient.

Endpoint: POST /api/Visitation/CreateEncounter/


### Submit Patient Vitals:

Allows nurses to submit patient vitals including blood pressure, temperature, pulse rate, and SP02.

Endpoint: POST /api/Vitals/CreatePatientVitals/


### View List of Patients:

Provides a list of patients for doctors to view.

Endpoint: GET /api/Register/


### View Patient Details:

Allows doctors to view detailed information about a specific patient.

Endpoint: GET /api/Register/patientDetails/int:pk/

### Update Patient Details:

Allows updating patient details

Endpoint: PUT /api/Register/updatePatient/int:pk/

### View List of Encounters:

Provides a list of patient encounters.

Endpoint: GET /api/Visitaion/

### View Encounter Details:

Allows viewing detailed information about a specific encounter.

Endpoint: GET /api/Visitaion/PatientEncounterDetails/int:pk/

### Update Encounter Details:

Allows updating encounter details.

Endpoint: PUT /api/Visitaion/PatientEncounterUpdate/int:pk/

### Delete Encounter:

Allows deleting an encounter.

Endpoint: DELETE /api/Visitation/DeletePatientEncounter/int:pk/

### View List of Patient Vitals:

Provides a list of patient vitals.

Endpoint: GET /api/Vitals/

### View Patient Vitals Details:

Allows viewing detailed information about a specific patient's vitals.

Endpoint: GET /api/Vitals/PatientVitalsDetails/int:pk/

### Update Patient Vitals:

Allows updating patient vitals.

Endpoint: PUT /api/Vitals/PatientVitalsUpdate/int:pk/

## Project Structure:


|-- Hospital/

    |-- patient/
    |   |-- models.py
    |   |-- serializers.py
    |   |-- views.py
    |   |-- urls.py
    |-- migrations/
    |-- __init__.py
    |-- settings.py
    |-- urls.py
    |-- wsgi.py
|-- README.md

## Usage:

### Clone the repository.
clone: https://github.com/Eddie-hanson/-Electronic-Medical-Record-System.git

Set up the Django project with PostgreSQL as the database backend.
Implement the models, serializers, and views for various functionalities as mentioned above.
Define the URL patterns for the endpoints.
Run the Django development server.
Test the endpoints using tools like Postman or through the frontend system integration.

Author: Edward Koffi Hanson

Date: 1st April 2024








