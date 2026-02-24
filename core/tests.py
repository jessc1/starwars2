import time

import pytest
from django.core.cache import cache
from rest_framework import status

from configtest import clear_cache, client
from fixtures.film import film
from fixtures.people import people
from fixtures.user import user


class TestPeopleViewSet:
    endpoint ='/api/people/'

    def test_list(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK

    def test_list_response_time(self, client, user):
        client.force_authenticate(user=user)
        start_time = time.perf_counter()
        response = client.get(self.endpoint)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        assert response.status_code == status.HTTP_200_OK
        assert elapsed_time < 0.5      
    
    def test_retrieve(self, client, user, people):        
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(people.id) + "/")
        assert response.data['name'] == people.name
    
    @pytest.mark.django_db
    def test_cached_people(self, client, clear_cache, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK

        response1 = client.get(self.endpoint)
        assert response1.status_code == status.HTTP_200_OK
  