from django.db import models

#	Setiap merubah model maka harus melakukan 'Makemigrates' pada ComandPromt dilanjutkan dengan 'migrate'
class Task(models.Model):
	name = models.TextField(default='')
	status = models.TextField(default='pending')
	keterangan = models.TextField(default='Selesai')