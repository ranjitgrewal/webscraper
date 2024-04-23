from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request

# Create your tests here.


class TestStuff(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_the_stuff(self):
        req = Request(self.factory.get("/scrape"))
