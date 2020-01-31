from rest_framework.generics import ListAPIView
from rest_framework import viewsets, permissions
from exercises.models import Exercise
from .serializers import ExerciseSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    # queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.exercises.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ExerciseDetailView(ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
