import pytest
from rest_framework import status
from configtest import client, clear_cache
from fixtures.user import user
from django.core.cache import cache

class TestPeopleViewSet:
    endpoint ='/api/people/'

    def test_list(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
    
    @pytest.mark.django_db
    def test_cached_people(self, client, clear_cache, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK

        response1 = client.get(self.endpoint)
        assert response1.status_code == status.HTTP_200_OK
  