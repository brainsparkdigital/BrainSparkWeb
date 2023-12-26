# posts/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Service

class ServiceModelTest(TestCase):
    def setUp(self):
        # Create a sample Service instance for testing
        self.service = Service.objects.create(
            name='Test Service',
            description='This is a test service.',
            detail='This is the detailed information about the test service.'
        )

    def test_service_str_method(self):
        # Check if the __str__ method returns the expected string
        self.assertEqual(str(self.service), 'Test Service')

    def test_service_get_absolute_url(self):
        # Check if the get_absolute_url method returns the correct URL
        expected_url = reverse('service_detail', args=[str(self.service.id)])
        self.assertEqual(self.service.get_absolute_url(), expected_url)

    # Add more tests as needed to cover other aspects of the Service model
