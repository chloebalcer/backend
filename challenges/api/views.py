from rest_framework.generics import ListAPIView

from challenges.models import Challenge
from .serializers import ChallengeSerializer


class ChallengeListView(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class ChallengeDetailView(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
