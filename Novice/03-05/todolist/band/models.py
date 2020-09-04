from django.db import models

class Genre(models.Model):
	genre = models.TextField(default='(Genre)')
	tahun = models.TextField(default='(Tahun)')
	negara_asal = models.TextField(default='(Negara Asal)')


class Band(models.Model):
	nama_band = models.TextField(default='(Nama Band)')
	aliran = models.TextField(default='(Aliran)')
	negara_asal = models.TextField(default='(Negara Asal)')
	tahun = models.TextField(default='(Tahun)')
	label = models.TextField(default='(Label)')
	status = models.TextField(default='(Status)')
