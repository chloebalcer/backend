from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CHOICES = (
        (11, 'Etudiant'),
        (12, 'Professeur'),
        (13, 'Entreprise'),
    )
    status = models.CharField(max_length=50, choices=CHOICES)
    student_code = models.CharField(max_length=50, null=True, blank=False)

