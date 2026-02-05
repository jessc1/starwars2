from rest_framework import routers

from .viewsets import LoginViewSet, RegisterViewSet

router = routers.SimpleRouter()
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/logout', LoginViewSet, basename='auth-logout')

urlpatterns = [
    *router.urls,
    ]
