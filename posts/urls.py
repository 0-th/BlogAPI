from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register(prefix='users', viewset=UserViewSet, basename='users')
router.register(prefix='', viewset=PostViewSet, basename='posts')

urlpatterns = router.urls
