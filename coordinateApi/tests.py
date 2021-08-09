from django.test import TestCase
from .models import Coordinates

# Create your tests here.

class CoordinatesTestCase(TestCase):
    """This class defines the test suite for the Coordinates model."""

    @classmethod
    def setUp(cls):
        """Define the test client and other test variables."""
        Coordinates.objects.create(submitted_coordinate = '(1,3,),(3,4),(6,7),(8,12),(45,78),(7,12),(9,5)',closet_paircoordinates  ='(8, 12), (7, 12)')
    
        
       

    def test_model_submitted_coordinate(self):
        testcordinate = Coordinates.objects.get(id =1 )
        expected_cooridnatelist = f'{testcordinate.submitted_coordinate}'
        self.assertEqual(expected_cooridnatelist,'(1,3,),(3,4),(6,7),(8,12),(45,78),(7,12),(9,5)')
    

    def test_model_closet_paircoordinates(self):
        testcordinate = Coordinates.objects.get(id =1 )
        test_expected_closet_paircoordinates = f'{testcordinate.closet_paircoordinates}'
        self.assertEqual(test_expected_closet_paircoordinates,'(8, 12), (7, 12)')
        

         








