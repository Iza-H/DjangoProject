
from django import forms
from photos.models import Photo


class PhotoForm(forms.ModelForm):
    """
    Form for a model Photos
    """

    class Meta:
        model = Photo
        exclude = []