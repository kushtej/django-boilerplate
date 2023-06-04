from django.test import TestCase
import json

# Create your tests here.

from rest_framework import status
from rest_framework.test import APIRequestFactory

from .views import ping

class PingViewTestCase(TestCase):

    def test_ping_view(self):
        factory = APIRequestFactory()
        request = factory.get('/ping/')
        response = ping(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        expected_data = {"success": True, "result": "Service is Active"}
        self.assertEqual(response_data, expected_data)