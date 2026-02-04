import requests
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import People, Film, Planet, Starship, Vehicle, Species, User
from .serializers import PeopleSerializer, FilmSerializer, PlanetSerializer, StarshipSerializer, VehicleSerializer, SpeciesSerializer, UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    http_method_names = ('get')
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
    def get_object_by_id(self):
        obj = User.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj



class PeopleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for listing and retrieving, search and filter characters
    """
      
    http_method_names = ('get')    
    serializer_class = PeopleSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    search_fields = ['name', 'hair_color']

    def get_queryset(self):
        queryset = People.objects.all()
        return queryset
    
    def get_object_by_id(self):
        obj = People.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for listing and retrieving, search and filter movies
    """
      
    http_method_names = ('get')    
    serializer_class = FilmSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'episode_id']
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Film.objects.all()
        return queryset
    
    def get_object_by_id(self):
        obj = Film.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

class PlanetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for listing and retrieving, search and filter planets
    """
      
    http_method_names = ('get')    
    serializer_class = PlanetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'climate']
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Planet.objects.all()
        return queryset
    
    def get_object_by_id(self):
        obj = Planet.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


  
class StarshipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for listing and retrieving, search and filter starships
    """
      
    http_method_names = ('get')    
    serializer_class = StarshipSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['starship_class']
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Starship.objects.all()
        return queryset
    
    def get_object_by_id(self):
        obj = Starship.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class VehicleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for listing and retrieving, search and filter vehicles
    """
      
    http_method_names = ('get')    
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Vehicle.objects.all()
        return queryset
    
    def get_object_by_id(self):
        obj = Vehicle.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for listing and retrieving, search and filter species
    """
      
    http_method_names = ('get')    
    serializer_class = SpeciesSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Species.objects.all()
        return queryset
    
    def get_object_by_id(self):
        obj = Species.objects.get(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj    

    