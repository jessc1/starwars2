from unittest.mock import Mock, patch

import pytest
from django.urls import reverse
from rest_framework import status

from configtest import client
from fixtures.user import user


class TestPeopleViewSet:
    endpoint ='/api/people/'

    def test_list(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
    
    def test_retrieve(self, client, user):
        
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(people.id)+ "/")
        assert response.data['id'] == people.id
        assert response.data['people'] == people.name