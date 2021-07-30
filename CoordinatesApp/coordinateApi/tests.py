from django.test import TestCase
from .models import Coordinates
from django.core.urlresolvers import reverse
# Create your tests here.

class CoordinatesTestCase(TestCase):
    """This class defines the test suite for the Coordinates model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.coordinatesListsubmitted = "(1,3,),(3,4),(6,7),(8,12),(45,78),(7,12),(9,5)"
        self.twoclosepoints  ="[(8, 12), (7, 12)]"
        self. coordinates= Coordinates(self.coordinatesListsubmitted,self.twoclosepoints)

    def test_model_can_create_a_Coordinates(self):
        """Test the Coordinates model can create a Coordinates with two closepoints."""
        old_count = Coordinates.objects.count()
        self.coordinates.save()
        new_count = Coordinates.objects.count()
        self.assertNotEqual(old_count, new_count)






class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.coordinatelist_data = {'submitted_coordinate': '(1,3,),(3,4),(6,7),(8,12),(45,78),(7,12),(9,5)','closet_paircoordinates':'[(8, 12), (7, 12)]'}
        self.response = self.client.post(
            reverse('/coordinates'),
            self.coordinatelist_data,
            format="json")

    def test_api_can_create_a_coordinatet(self):
        """Test the api has Coordinates creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)