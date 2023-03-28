from unittest import TestCase
from primu.models import Owners
from rest_framework.test import APIRequestFactory, APITestCase
from primu.views import owners_list, owners_detail

class OwnerListViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_teachers = 30
        for o_id in range(number_of_teachers):
            Owners.objects.create(name=f"ownerul_{o_id}", addres="Cluj-Napoca", cnp="123")

    def test_url_exists(self):
        response = self.client.get("http://127.0.0.1:8000/owners/")

        self.assertEqual(response.status_code, 200)

    def test_count_correctly_returned(self):
        response = self.client.get("http://127.0.0.1:8000/owners/")
        self.assertEqual(len(response.data), 30)
