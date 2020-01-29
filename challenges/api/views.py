from rest_framework.generics import ListAPIView

from challenges.models import Challenge
from .serializers import ChallengeSerializer
from rest_framework import viewsets, permissions


class ChallengeViewSet(ListAPIView):
    # queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.challenges.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChallengeDetailView(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
