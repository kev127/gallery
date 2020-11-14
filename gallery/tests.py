from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.locations = Location(name='Nairobi')
        self.locations.save_location()

        self.cars = Category(name = 'cars')
        self.cars.save_category()

        self.new_image=Image(image_name='car',image_description='1300cc engine',image_category=self.cars,image_location=self.locations)
        self.new_image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_get_image(self):
        all_image = Image.get_image()
        self.assertTrue(len(all_image)>0)

    def test_filter_by_location(self):
        test_location_id = 6
        images_location = Image.filter_by_location(test_location_id) 
        self.assertTrue(len(image_location) == 0)   

    def test_delete_image(self):
        self.new_image.save_image()
        image1 = Image.objects.all()
        self.assertEqual(len(image1),1)

class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location)) 

    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)    