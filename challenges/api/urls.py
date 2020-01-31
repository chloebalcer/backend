from rest_framework import routers

from .views import ChallengeViewSet

router = routers.DefaultRouter()
router.register('challenges', ChallengeViewSet, 'challenges')
# router.register('<The URL prefienx>', <The viewset class>, '<The URL name>')

urlpatterns = router.urls
