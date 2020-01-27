from rest_framework.generics import ListAPIView

from exercises.models import Exercise
from .serializers import ExerciseSerializer


class ExerciseListView(ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetailView(ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
