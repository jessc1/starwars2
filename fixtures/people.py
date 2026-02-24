import pytest

from core.models import People
from fixtures.film import film


@pytest.fixture
def people(db, film):
    p = People.objects.create(name='Darth Vader', 
                                height="202", 
                                mass="136", 
                                hair_color="none",
                                skin_color="white", 
                                birth_year="41.9BBY",
                                gender="male",
                                homeworld="https://swapi.dev/api/planets/1/",
                                species=[],
                                vehicles=[],
                                starships=["https://swapi.dev/api/starships/13/"],
                                url="https://swapi.dev/api/people/1/")
    p.films.set([film])
    return p                                