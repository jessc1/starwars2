import requests
from django.core.management.base import BaseCommand
from core.models import People, Film, Planet, Vehicle, Species, Starship

class Command(BaseCommand):
    help = 'Imports Star Wars data from SWAPI'

    def get_characters(self, *args, **kwargs):
        url = 'https://swapi.dev/api/people/'
        while url:
            response = requests.get(url).json()
            for person in response['results']:
                People.objects.get_or_create(
                    name=person['name'],
                    mass = person['mass'],
                    height= person['height'],
                    hair_color = person['hair_color'],
                    skin_color = person['skin_color'],
                    eye_color = person['eye_color'],
                    birth_year = person['birth_year'],
                    gender=person['gender'],
                    homeworld = person['homeworld'],                    
                    created = person['created'],
                    films = person['films'],
                    url = person['url'],    
                )
            url = response['next']
        self.stdout.write(self.style.SUCCESS('characters data imported'))
    
    def get_films(self, *args, **kwargs):
        url = 'https://swapi.dev/api/films/'
        while url:
            response = requests.get(url).json()
            for film in response['results']:
                Film.objects.get_or_create(
                    title=film['title'],
                    episode_id=film['episode_id'],
                    opening_crawl=film['opening_crawl'],
                    director=film['director'],
                    producer=film['producer'],
                    release_date=film['release_date'],
                    characters = film['characters'],
                    planets = film['planets'],
                    starships=film['starships'],
                    vehicles = film['vehicles'],                    
                    species = film['species'],
                    created = film['created'],
                    edited = film['edited'],
                    url = film['url'],    
                )
            url = response['next']
        self.stdout.write(self.style.SUCCESS('film data imported'))
    
    def get_planets(self, *args, **kwargs):
        url = 'https://swapi.dev/api/planets/'
        while url:
            response = requests.get(url).json()
            for planet in response['results']:
                Planet.objects.get_or_create(
                    name=planet['name'],
                    rotation_period = planet['rotation_period'],
                    orbital_period= planet['orbital_period'],
                    diameter = planet['diameter'],
                    climate = planet['climate'],
                    gravity = planet['gravity'],
                    terrain=planet['terrain'],
                    surface_water = planet['surface_water'],
                    population = planet['population'],
                    #residents = planet['residents'],
                    films = planet['films'],
                    url = planet['url'],    
                )
            url = response['next']
        self.stdout.write(self.style.SUCCESS('planets data imported'))
    

    def get_vehicles(self, *args, **kwargs):
        url = 'https://swapi.dev/api/vehicles/'
        while url:
            response = requests.get(url).json()
            for vehicle in response['results']:
                Vehicle.objects.get_or_create(
                    name=vehicle['name'],
                    model = vehicle['model'],
                    manufacturer= vehicle['manufacturer'],
                    cost_in_credits = vehicle['cost_in_credits'],
                    length = vehicle['length'],
                    max_atmosphering_speed = vehicle['max_atmosphering_speed'],
                    crew = vehicle['crew'],
                    passengers=vehicle['passengers'],
                    cargo_capacity = vehicle['cargo_capacity'],
                    consumables = vehicle['consumables'],
                    vehicle_class = vehicle['vehicle_class'],
                    pilots = vehicle['pilots'],
                    

                )
            url = response['next']
        self.stdout.write(self.style.SUCCESS('vehicles data imported'))
    
    def get_species(self, *args, **kwargs):
        url = 'https://swapi.dev/api/species/'
        while url:
            response = requests.get(url).json()
            for species in response['results']:
                Species.objects.get_or_create(
                    name=species['name'],
                    classification = species['classification'],
                    designation= species['designation'],
                    average_height = species['average_height'],
                    skin_colors = species['skin_colors'],
                    eye_colors = species['eye_colors'],
                    hair_colors = species['hair_colors'],
                    average_lifespan = species['average_lifespan'],
                    homeworld=species['homeworld'],
                    language = species['language'],
                    people = species['people'],
                    films = species['films'],                    
                    url = species['url'],    
                )
            url = response['next']
        self.stdout.write(self.style.SUCCESS(' species data imported'))
    
    def get_starships(self, *args, **kwargs):
        url = 'https://swapi.dev/api/starships/'
        while url:
            response = requests.get(url).json()
            for starship in response['results']:
                Starship.objects.get_or_create(
                    hyperdrive_rating=starship['hyperdrive_rating'],
                    MGLT = starship['MGLT'],
                    starship_class= starship['starship_class'],
                    pilots = starship['pilots'],
                   
                )
            url = response['next']
        self.stdout.write(self.style.SUCCESS(' starships data imported'))
    
    def handle(self, *args, **options):
        self.get_characters()
        self.get_films()
        #self.get_planets()
        #self.get_starships()
        #self.get_vehicles()
        #self.get_species()
        
        self.stdout.write(self.style.SUCCESS('finish import'))




        





    

    