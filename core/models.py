from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=100)
    orbital_period = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)
    gravity = models.CharField(max_length=100)
    terrain = models.CharField(max_length=100)
    surface_water = models.CharField(max_length=200)
    population = models.CharField(max_length=100)
    residents = models.URLField(models.URLField(max_length=1000)) 
    films = models.URLField(models.URLField(max_length=1000)) 
    url = models.URLField(max_length=500)          
    
    def __str__(self):
        
        return self.name

class Transport(models.Model):
    
    name = models.CharField(max_length=100)
    model =models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    cost_in_credits= models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    max_atmosphering_speed = models.CharField(max_length=100) 
    crew = models.CharField(max_length=100)
    passengers = models.CharField(max_length=100)
    cargo_capacity = models.CharField(max_length=100)
    consumables = models.CharField(max_length=100)   

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=300)
    episode_id=models.IntegerField()
    opening_crawl = models.TextField()
    director=models.CharField(max_length=300)
    producer=models.CharField(max_length=300)
    release_date=models.DateTimeField()
    characters = models.URLField(max_length=4000)  
    planets =models.URLField(max_length=1000)  
    starships = models.URLField(max_length=1000)        
    vehicles = models.URLField(max_length=1000)  
    species = models.URLField(max_length=1000)  
    created=models.DateTimeField()
    edited = models.DateTimeField()                   
    url = models.URLField(max_length=1000)     

    def __str__(self):
        return self.title  

class People(models.Model):
    
    name=models.CharField(max_length=100)
    height = models.CharField(max_length=100, blank=True)
    mass = models.CharField(max_length=100, blank=True)
    hair_color = models.CharField(max_length=100, blank=True)
    skin_color = models.CharField(max_length=100, blank=True)
    eye_color = models.CharField(max_length=100, blank=True)
    birth_year = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    homeworld = models.URLField(max_length=1000, default='homeworld')    
    films = models.URLField(max_length=1000, default='films') 
    species = models.URLField(max_length=1000,default='species')
    vehicles = models.URLField(max_length=1000, default='vehicle')
    starships = models.URLField(max_length=1000, default='starship')
    created=models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.url


class Vehicle(Transport):
    vehicle_class = models.CharField(max_length=200)
    

class Species(models.Model):
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    average_height =models.CharField(max_length=200)
    skin_colors = models.CharField(max_length=200)
    hair_colors = models.CharField(max_length=200)
    eye_colors = models.CharField(max_length=200)
    average_lifespan = models.CharField(max_length=200)
    homeworld = models.URLField(max_length=1000, null=True)  
    language = models.CharField(max_length=100)
    people = models.URLField(max_length=1000)
    films = models.URLField(max_length=1000, default='films')    
    url = models.URLField(default='url')

class Starship(Transport):
    hyperdrive_rating = models.CharField(max_length=100)
    MGLT = models.CharField(max_length=100)
    starship_class = models.CharField(max_length=100)
    pilots =  models.URLField(max_length=1000) 



