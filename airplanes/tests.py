from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from airplanes.models import Aeroplane

class AirplaneViewsTest(TestCase):
    """
    Test case for testing API views related to Aeroplanes.

    Attributes:
    - client: Test client for making API requests.
    - url: URL endpoint for Aeroplane list and create operations.
    - valid_data: Valid data for creating an Aeroplane.
    - airplane: Instance of the Aeroplane model for testing.
    """

    def setUp(self):
        """
        Set up necessary objects and configurations for testing.
        """
        self.client = APIClient()
        self.url = reverse('aeroplane-list-create')
        self.valid_data = {'id': 1, 'passenger_assumptions': 100}
        self.airplane = Aeroplane.objects.create(id=1, passenger_assumptions=100)

    def test_update_airplane(self):
        """
        Test updating an existing Aeroplane through the API.

        Ensures successful update and proper field values.
        """
        update_data = {'id': self.airplane.id, 'passenger_assumptions': 150}
        response = self.client.put(reverse('aeroplane-detail', kwargs={'pk': self.airplane.id}), update_data, format='json')
        
        if response.status_code != status.HTTP_200_OK:
            print(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.airplane.refresh_from_db()
        self.assertEqual(self.airplane.passenger_assumptions, 150)

    def test_partial_update_airplane(self):
        """
        Test partially updating an existing Aeroplane through the API.

        Ensures successful partial update and proper field values.
        """
        update_data = {'id':self.airplane.id,'passenger_assumptions': 120}
        response = self.client.patch(reverse('aeroplane-detail', kwargs={'pk': self.airplane.id}), update_data, format='json')
        
        if response.status_code != status.HTTP_200_OK:
            print(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.airplane.refresh_from_db()
        self.assertEqual(self.airplane.passenger_assumptions, 120)

    def test_delete_airplane(self):
        """
        Test deleting an existing Aeroplane through the API.

        Ensures successful deletion and non-existence in the database.
        """
        response = self.client.delete(reverse('aeroplane-detail', kwargs={'pk': self.airplane.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Aeroplane.objects.filter(id=self.airplane.id).exists())

    def test_invalid_update_data(self):
        """
        Test updating an existing Aeroplane with invalid data through the API.

        Ensures a proper error response for invalid data.
        """
        invalid_update_data = {'passenger_assumptions': -10}
        response = self.client.patch(reverse('aeroplane-detail', kwargs={'pk': self.airplane.id}), invalid_update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_single_airplane(self):
        """
        Test retrieving details of a single Aeroplane through the API.

        Ensures successful retrieval and matching object details.
        """
        response = self.client.get(reverse('aeroplane-detail', kwargs={'pk': self.airplane.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.airplane.id)

    def test_create_airplane(self):
        """
        Test creating a new Aeroplane through the API.

        Ensures successful creation and existence in the database.
        """
        new_airplane_data = {'id': 2, 'passenger_assumptions': 120}
        response = self.client.post(self.url, new_airplane_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Aeroplane.objects.filter(id=2).exists())

    def test_list_airplanes(self):
        """
        Test listing all Aeroplanes through the API.

        Ensures a proper response with the correct number of objects.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Adjust based on your initial setup

    def test_invalid_create_data(self):
        """
        Test creating a new Aeroplane with invalid data through the API.

        Ensures a proper error response for invalid creation data.
        """
        invalid_data = {'id': 2, 'passenger_assumptions': -10}
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


