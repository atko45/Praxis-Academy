from django.forms import ModelForm

from . import models

class GenreForm(ModelForm):
    class Meta:
        model = models.Genre
        exclude = []

class BandForm(ModelForm):
    class Meta:
        model = models.Band
        exclude = []