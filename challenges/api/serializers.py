from rest_framework import serializers
from challenges.models import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('title', 'description', 'language', 'starting_date', 'ending_date',
                  'is_coding_game', 'allocated_time', 'subject', 'contact_mail', 'pseudo', 'auto_correction')
