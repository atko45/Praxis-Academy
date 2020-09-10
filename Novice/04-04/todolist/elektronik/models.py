from django.db import models

class Elektronik(models.Model):
	elek_image = models.CharField(default='Image', max_length= 255)
	elek_name = models.CharField(default='Name', max_length= 255)
	elek_stock = models.CharField(default='Stock', max_length= 255)
	elek_price = models.CharField(default='Gambar', max_length= 255)
	elek_info = models.CharField(default='Info', max_length= 255)