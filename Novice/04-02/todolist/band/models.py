from django.db import models

class Genre(models.Model):
	genre = models.CharField(default='(Genre)', max_length= 255)
	tahun = models.CharField(default='(Tahun)', max_length= 255)
	negara_asal = models.CharField(default='(Negara Asal)', max_length= 255)


class Band(models.Model):
	nama_band = models.CharField(default='(Nama Band)', max_length= 255)
	aliran = models.CharField(default='(Aliran)', max_length= 255)
	negara_asal = models.CharField(default='(Negara Asal)', max_length= 255)
	tahun = models.CharField(default='(Tahun)', max_length= 255)
	label = models.CharField(default='(Label)', max_length= 255)
	status = models.CharField(default='(Status)', max_length= 255)
