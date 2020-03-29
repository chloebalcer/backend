from rest_framework import routers
from django.urls import path
from .views import ChallengeViewSet, ChallengeDetailView

router = routers.DefaultRouter()
router.register('challenges', ChallengeViewSet, base_name='challenges')
router.register('<pk>', ChallengeDetailView, base_name='challengesdetail')
# router.register('<The URL prefienx>', <The viewset class>, '<The URL name>')

urlpatterns = router.urls

# urlpatterns = [
#     path('/', ChallengeViewSet,
#     path('<pk>', ChallengeDetailView)

# ]
