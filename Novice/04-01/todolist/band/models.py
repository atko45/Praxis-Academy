from django.db import models

class Band(models.Model):
	nama_band = models.CharField(default='(Nama Band)', max_length = 255)
	aliran = models.CharField(default='(Aliran)', max_length = 255)
	negara_asal = models.CharField(default='(Negara Asal)', max_length = 255)
	personil = models.CharField(default='(Personil)', max_length = 255)
	posisi = models.CharField(default='(Posisi)', max_length = 255)
	status = models.CharField(default='(Status)', max_length = 255)



