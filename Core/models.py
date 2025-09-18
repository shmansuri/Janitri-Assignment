from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin","admin"),
        ("doctor","doctor"),
        ("operator","operator"))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operator')

    def __str__(self):
        return self.username


class Patient(models.Model):
    GENDER_CHOICES = (
        ("male","Male"),
        ("female","Female"),
        ("other","Other"),)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField(blank=True)
    created_by = models.ForeignKey('Core.User', on_delete=models.SET_NULL, null=True, related_name='patients')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} ({self.id})"


class HeartRate(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='heartrates')
    bpm = models.PositiveIntegerField()
    recorded_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-recorded_at']


    def __str__(self):
        return f"HR {self.bpm} for {self.patient_id} at {self.recorded_at}"