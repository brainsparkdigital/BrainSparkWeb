# posts/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import PortFolio

class PortFolioModelTest(TestCase):
    def setUp(self):
        self.portfolio = PortFolio.objects.create(
            title='Test Portfolio',
            body='This is a test portfolio body content.'
        )

    def test_portfolio_creation(self):
        self.assertEqual(self.portfolio.title, 'Test Portfolio')
        self.assertEqual(self.portfolio.body, 'This is a test portfolio body content.')
        self.assertEqual(str(self.portfolio), 'Test Portfolio')

    def test_get_absolute_url(self):
        expected_url = reverse('portfolio_detail', args=[str(self.portfolio.id)])
        self.assertEqual(self.portfolio.get_absolute_url(), expected_url)
