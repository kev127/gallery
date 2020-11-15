from django.forms import ModelForm      
from .models import Image
from cloudinary.forms import CloudinaryFileField    

class ImageForm(ModelForm):
  class Meta:
      model = Image
      fields = '__all__'
  gallery = CloudinaryFileField(
        # attrs = { 'style': "margin-top: 30px" }, 
        options = { 
            'tags': "directly_uploaded",
            'crop': 'limit', 'width': 1000, 'height': 1000,
            'eager': [{ 'crop': 'fill', 'width': 150, 'height': 100 }]
        })