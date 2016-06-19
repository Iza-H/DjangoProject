
from django import forms
from django.core.exceptions import ValidationError
from photos.models import Photo
from photos.settings import BADWORDS

class PhotoForm(forms.ModelForm):
    """
    Form for a model Photos
    """

    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        cleaned_data = super(PhotoForm, self).clean()
        description = cleaned_data.get('description', '')


        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError(u'Word {} prohibited'.format(badword))

        return cleaned_data