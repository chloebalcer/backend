from rest_framework import routers

from .views import ExerciseViewSet

router = routers.DefaultRouter()
router.register('exercises', ExerciseViewSet, 'exercises')
# router.register('<The URL prefienx>', <The viewset class>, '<The URL name>')

urlpatterns = router.urls
