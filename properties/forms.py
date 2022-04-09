from django.forms import ModelForm
from .models import Image


class ImageForm(ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')