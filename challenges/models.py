from django.db import models
from accounts.models import User


class Challenge(models.Model):
    LANGUAGES = (
        (4, 'Python'),
        (5, 'R'),
    )
    CHALLENGE_TYPE = (
        (1, 'Coding Game'),
        (2, 'Professional'),
        (3, 'Community'),
    )
    title = models.CharField(max_length=120)
    description = models.TextField()  # Enonce du challenge
    language = models.IntegerField(choices=LANGUAGES)
    starting_date = models.DateField(blank=True)
    ending_date = models.DateField(blank=True)
    challenge_type = models.CharField(max_length=50, choices=CHALLENGE_TYPE)
    allocated_time = models.TimeField(blank=True, null=True)
    contact_mail = models.EmailField(max_length=120)
    owner = models.ForeignKey(
        User, related_name="challenges", on_delete=models.CASCADE, null=True, blank=True)
    # Activer la correction automatique
    auto_correction = models.BooleanField(default=False)

    def __str__(self):
        return self.title
