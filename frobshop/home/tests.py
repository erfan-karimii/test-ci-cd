from django.test import TestCase 
from django.urls import reverse
# Create your tests here.

class TestHomeView(TestCase):
    def test_home_view(self):
        url = reverse('home_app:test-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)