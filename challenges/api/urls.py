from django.urls import path

from .views import ChallengeViewSet, ChallengeDetailView

urlpatterns = [
    path('', ChallengeViewSet.as_view()),
    path('/<pk>', ChallengeDetailView.as_view())
]
