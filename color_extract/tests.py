from django.test import TestCase,Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import StripFile
from .views import upload_image
from .extract_color import extract_colors
import os
# Create your tests here.


class StripFileTestCase(TestCase):

    def setUp(self):
        self.image_data = b'/strip_images/image3.jpg'
        self.image_file = SimpleUploadedFile(
            'uploads/test_image.jpg', self.image_data, content_type='image/jpeg')
        self.color_val = {"URO": [174, 170, 167], "BIL": [152, 149, 144], "KET": [203, 200, 191], "BLD": [197, 198, 193], "PRO": [
            189, 186, 167], "NIT": [186, 179, 169], "LEU": [84, 78, 78], "GLU": [143, 136, 120], "SG": [170, 165, 162], "PH": [161, 155, 155]}
        self.image_path = "./strip_images/image3.jpg"
        self.abs_path = os.path.abspath(self.image_path)


    def test_data_upload(self):
        '''
        makes sure data is uploaded to database
        '''
        StripFile_instance = StripFile.objects.create(
            image=self.image_file, color_values=self.color_val)

        saved_instance = StripFile.objects.filter(
            id=StripFile_instance.id).first()

        self.assertIsNotNone(saved_instance)
        self.assertEqual(saved_instance.color_values, self.color_val)
        self.assertTrue(saved_instance.image)

    def test_extract_colors(self):
        '''
        check if extract_colors is giving accurate output.
        '''

        image_file = open(self.abs_path, "rb")
        
        test_extracted_color = extract_colors(image_file)

        self.assertIsInstance(test_extracted_color, dict)
        self.assertEqual(test_extracted_color,self.color_val)

    def test_upload_image(self):

        client = Client()
        
        # Open the test image file and create a POST request with the image file
        with open(self.abs_path, 'rb') as image_file:
            response = client.post(reverse('upload-image'), {'file': image_file})
        
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Retrieve the created StripFile object from the database
        strip_file = StripFile.objects.first()
        
        # Assert that the StripFile object is created
        self.assertIsNotNone(strip_file)
        
        # Assert that the extracted_colors field of the StripFile object is populated
        self.assertIsNotNone(strip_file.color_values)
        
        
        self.assertEqual(strip_file.color_values,self.color_val)



        
        
