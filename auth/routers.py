from rest_framework import routers
from .viewsets import RegisterViewSet, LoginViewSet


router = routers.SimpleRouter()
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')


urlpatterns = [
    *router.urls,
    ]