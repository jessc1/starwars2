from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import IntegerField, Max, Q, Count
from django.db.models.functions import Cast
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

    @staticmethod
    def get_tallest_character():
        filtered_people = People.objects.exclude(
            Q(height='unknown') | Q(height__isnull=True) | Q(height='')
        )
        tallest_person = filtered_people.annotate(
            max_height=Max(Cast('height', IntegerField()))
        ).order_by('-max_height').first()
        return tallest_person
    
    @staticmethod
    def get_gender_count():
        return People.objects.exclude(gender__isnull=True).annotate(count=Count('gender')).values('gender')
     
       
        
