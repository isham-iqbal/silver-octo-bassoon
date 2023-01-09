from django.test import TestCase


from polls.models import Bar

class BarTestCase(TestCase):

    def setUp(self):

        self.data = {"value": "test"}
    
    def test_bar_insertion(self):

        self.client.post("/api/v1/bar/", data=self.data, format="json")
        
        self.client.post("/api/v1/bar/", data=self.data, format="json")
        

