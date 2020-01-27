from django.db import models

class Challenge(models.Model):
    LANGUAGES = (
        (13, 'Python'),
        (14, 'R'),
    )
    title = models.CharField(max_length=120)
    description = models.TextField() # Enonce du challenge
    language = models.IntegerField(max_length=50, choices=LANGUAGES)
    starting_date = models.DateField(blank= True)
    ending_date = models.DateField(blank= True)
    is_coding_game = models.BooleanField(default=False) 
    allocated_time = models.TimeField(blank= True, null =True)
    subject = models.CharField(max_length=120) # Type de challenge
    contact_mail = models.EmailField(max_length=120)
    pseudo = models.CharField(max_length=120)
    auto_correction = models.BooleanField(default=False)  # Activer la correction automatique
    
    def __str__(self):
        return self.title

