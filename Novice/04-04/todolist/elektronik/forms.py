from django.forms import ModelForm

from . import models

class ElektronikForm(ModelForm):
    class Meta:
        model = models.Elektronik
        exclude = []