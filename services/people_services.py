from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework.exceptions import NotFound, ValidationError
from core.models import People
from core.serializers import PeopleSerializer

class PeopleService:
    @staticmethod
    def list():
        return People.objects.all()

    @staticmethod
    def get(user_id):
        try:                       
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise NotFound("User not found")