from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator
from accounts.models import User


class Exercise(models.Model):
    LEVEL = (
        ("1", '1'),
        ("2", '2'),
        ("3", '3'),
        ("4", '4'),
        ("5", '5')
    )
    title = models.CharField(max_length=120, blank=False)
    level = models.IntegerField(choices=list(
        zip(range(1, 6), range(1, 6))))

    description = models.TextField(null=False, blank=False)  # enonce exercice
    # mots clés séparés par une virgule
  
    owner = models.ForeignKey(
        User, related_name="exercises", on_delete=models.CASCADE, null=True, blank=True)
    # Activer la correction automatique
    file = models.FileField(blank=True, null=True,
                            upload_to="corrections/%Y/%m/$D/", validators=[FileExtensionValidator(allowed_extensions=['pdf', 'tex', 'py', 'r'])])

    def __str__(self):
        return self.title
