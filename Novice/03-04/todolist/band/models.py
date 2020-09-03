from django.db import models

class Band(models.Model):
	nama_band = models.TextField(default='(Nama Band)')
	aliran = models.TextField(default='(Aliran)')
	negara_asal = models.TextField(default='(Negara Asal)')
	personil = models.TextField(default='(Personil)')
	posisi = models.TextField(default='(Posisi)')
	status = models.TextField(default='(Status)')


class Keterangan(models.Model):
	tahun = models.TextField(default='(tahun)')
	label = models.TextField(default='(label)')



