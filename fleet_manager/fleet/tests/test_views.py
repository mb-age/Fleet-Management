from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from ..models import Vehicle, Driver


class VehicleAPITest(APITestCase):
    def setUp(self):
        # Creating a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        # Obtaining a token for a user
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.driver = Driver.objects.create(
            first_name="Jan",
            last_name="Kowalski",
            license_number="XYZ123456",
            phone_number="123456789",
            address="ul. Nowa 5, Warszawa"
        )
        self.vehicle = Vehicle.objects.create(
            make="Toyota",
            model="Corolla",
            year=2018,
            vin="1HGCM82633A123456",
            registration_number="ABC1234",
            assigned_driver=self.driver
        )

    def test_get_vehicle(self):
        response = self.client.get(f'/api/vehicles/{self.vehicle.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['make'], 'Toyota')

    def test_create_vehicle(self):
        data = {
            "make": "Honda",
            "model": "Civic",
            "year": 2020,
            "vin": "2HGCM82633A456789",
            "registration_number": "JKL1234",
            "assigned_driver": self.driver.id
        }
        response = self.client.post('/api/vehicles/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['make'], 'Honda')


class RegisterAPITest(APITestCase):
    def test_register_user_success(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'password2': 'newpassword'
        }
        response = self.client.post('/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')

    def test_register_user_password_mismatch(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'password2': 'differentpassword'
        }
        response = self.client.post('/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
        self.assertIn('Passwords do not match.', response.data['non_field_errors'])


class VehicleUpdateDeleteAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.driver = Driver.objects.create(
            first_name="Jan",
            last_name="Kowalski",
            license_number="XYZ123456",
            phone_number="123456789",
            address="ul. Nowa 5, Warszawa"
        )
        self.vehicle = Vehicle.objects.create(
            make="Toyota",
            model="Corolla",
            year=2018,
            vin="1HGCM82633A123456",
            registration_number="ABC1234",
            assigned_driver=self.driver
        )

    def test_update_vehicle(self):
        data = {
            "make": "Honda",
            "model": "Civic",
            "year": 2020,
            "vin": "2HGCM82633A456789",
            "registration_number": "JKL1234",
            "assigned_driver": self.driver.id
        }
        response = self.client.put(f'/api/vehicles/{self.vehicle.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['make'], 'Honda')

    def test_delete_vehicle(self):
        response = self.client.delete(f'/api/vehicles/{self.vehicle.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Check if the vehicle has been deleted
        response = self.client.get(f'/api/vehicles/{self.vehicle.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ErrorHandlingAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.driver = Driver.objects.create(
            first_name="Jan",
            last_name="Kowalski",
            license_number="XYZ123456",
            phone_number="123456789",
            address="ul. Nowa 5, Warszawa"
        )
        self.vehicle = Vehicle.objects.create(
            make="Toyota",
            model="Corolla",
            year=2018,
            vin="1HGCM82633A123456",
            registration_number="ABC1234",
            assigned_driver=self.driver
        )

    def test_get_vehicle_not_found(self):
        response = self.client.get('/api/vehicles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_vehicle_missing_fields(self):
        data = {
            "make": "Honda",
            # 'model' field is missing
            "year": 2020,
            "vin": "2HGCM82633A456789",
            "registration_number": "JKL1234",
            "assigned_driver": self.driver.id
        }
        response = self.client.post('/api/vehicles/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('model', response.data)
