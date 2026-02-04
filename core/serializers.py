from rest_framework import serializers
from .models import People, Film, Planet, Starship, Vehicle, Species


class FilmSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Film
        fields = [
            'title', 'episode_id', 'director', 
                  'release_date', 'characters', 'url']


class PeopleSerializer(serializers.ModelSerializer):    
    
    class Meta:
                
        model = People
        fields = [
            'name', 'height', 'mass', 'hair_color', 
            'skin_color', 'eye_color', 'birth_year', 
            'gender', 'homeworld', 'films', 'url',            
        ]   



class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:           
        model = Starship
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_class',
        ]



class SpeciesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Species
        fields = [
             'name', 'classification', 'designation', 
            'average_height', 'skin_colors', 'hair_colors',
            'eye_colors', 'average_lifespan', 'films',
            'language',  'url']
  
            
