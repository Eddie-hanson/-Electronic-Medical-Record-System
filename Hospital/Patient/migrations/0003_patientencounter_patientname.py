# Generated by Django 5.0.3 on 2024-04-01 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_patientencounter_delete_patientencouter'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientencounter',
            name='PatientName',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Patient.registerpatient'),
            preserve_default=False,
        ),
    ]