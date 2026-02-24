from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Count, IntegerField, Max, Q
from django.db.models.functions import Cast
from rest_framework.exceptions import NotFound, ValidationError

from core.models import People
from core.serializers import PeopleSerializer


class PeopleService:
    @staticmethod
    def list():
        return People.objects.prefetch_related('films')

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
        return  People.objects.values('gender').annotate(count=Count('gender'))
    
    @staticmethod
    def get_oldest_character():
        people = People.objects.all().values('name', 'birth_year')

        def parse_birth_field(birth_str):
            if 'BBY' in birth_str:
                return -float(birth_str.replace('BBY', ''))
            elif 'ABY' in birth_str:
                return float(birth_str.replace('ABY', ''))
            else:
                return None
        
        sorted_people = sorted([p for p in people if parse_birth_field(p['birth_year']) is not None],
            key=lambda x: parse_birth_field(x['birth_year']),
            reverse=False)
        if sorted_people:
            oldest_character = sorted_people[0]
            return f"Name:{oldest_character['name']}, Birth Year: {oldest_character['birth_year']}"
        else:
            return "No character was found"   
        
        

            

     
       
        
