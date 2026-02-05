from rest_framework import routers

from .viewsets import (FilmViewSet, PeopleViewSet, PlanetViewSet,
                       SpeciesViewSet, StarshipViewSet, VehicleViewSet)

router = routers.SimpleRouter()

router.register(r'people', PeopleViewSet, basename='people')
router.register(r'films', FilmViewSet, basename='films')
router.register(r'planets', PlanetViewSet, basename='planets')
router.register(r'starships', StarshipViewSet, basename='starships')
router.register(r'vehicles', VehicleViewSet, basename='vehicles')
router.register(r'species', SpeciesViewSet, basename='species')
urlpatterns = [
    *router.urls,
]
