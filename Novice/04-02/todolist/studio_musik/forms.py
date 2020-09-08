from django.forms import ModelForm

from . import models

class StudiosForm(ModelForm):
    class Meta:
        model = models.Studios
        exclude = []