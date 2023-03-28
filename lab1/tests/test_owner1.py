from django.test import TestCase
from primu.models import Owners

class OwnerModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Owners.objects.create(name="Razvan",addres="rovine",cnp="1234")

    def test_string_method(self):
        teacher = Owners.objects.get(name="Razvan")
        expected_string = "Razvan"
        self.assertEqual(str(teacher), expected_string)