from django.db import models

# Create your models here.

class SaldoAwal(models.Model):
	i_saldo = models.IntegerField(default=0)