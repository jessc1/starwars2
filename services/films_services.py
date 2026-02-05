from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework.exceptions import NotFound, ValidationError
from core.models import Film
from core.serializers import PeopleSerializer

class FilmsService:
    @staticmethod
    def list():
        return Film.objects.all()