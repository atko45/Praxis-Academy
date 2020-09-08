from django.db import models

class Studios(models.Model):
	nama_label = models.CharField(default='(Nama Label)', max_length= 255)
	tahun_berdiri = models.CharField(default='(Tahun Berdiri)', max_length= 255)
	status_label = models.CharField(default='(Status Label)', max_length= 255)
	negara_label = models.CharField(default='(Status Label)', max_length= 255)