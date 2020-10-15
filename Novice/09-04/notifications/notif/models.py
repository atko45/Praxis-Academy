from django.db import models

class DataNotif(models.Model):
	nama = models.CharField(max_length=200)
	hutang = models.DecimalField(default=0, max_digits=10, decimal_places=0)
	tanggal_pinjam = models.DateField()
	tanggal_jatuh_tempo = models.DateField()
	keterangan = models.CharField(default='', max_length= 255)
		
