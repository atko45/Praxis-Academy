from django.forms import ModelForm

from . import models

class NotifForm(ModelForm):
    class Meta:
        model = models.DataNotif
        exclude = []