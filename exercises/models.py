from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator


class Exercise(models.Model):

    title = models.CharField(max_length=120, blank=False)
    level = models.IntegerField(choices=list(
        zip(range(1, 6), range(1, 6))), unique=True)

    description = models.TextField(null=False, blank=False)  # enonce exercice
    # mots clés séparés par une virgule
    key_words = ArrayField(models.CharField(
        max_length=25, blank=True), size=10)
    file = models.FileField(blank=True, null=True,
                            upload_to="corrections/%Y/%m/$D/", validators=[FileExtensionValidator(allowed_extensions=['pdf', 'tex', 'py', 'r'])])

    def __str__(self):
        return self.title
