from django.shortcuts import render, redirect
from . import models

# Create Saldo Awal

def c_saldo_awal(req):
	saldo_awal = models.SaldoAwal.objects.all()
	if req.POST:
		models.SaldoAwal.objects.create(i_saldo=req.POST['i_saldo'],)
		return redirect('/')

	return render(req, 'saldo/saldo_awal.html', 
		{
		'data': saldo_awal,
		})

# Read Saldo awal

def r_saldo_awal(req, id):
	saldo_awal = models.SaldoAwal.objects.filter(pk=id).first()

	return render(req, 'saldo/r_saldo_awal.html',
		{
		'data': saldo_awal,
		})

# Update Saldo Awal

def u_saldo_awal(req, id):
	if req.POST:
		models.SaldoAwal.objects.update(i_saldo=req.POST['i_saldo'],)
		return redirect('/')

	saldo_awal = models.SaldoAwal.objects.filter(pk=id).first()
	return render(req, 'saldo/u_saldo_awal.html',
		{
		'data': saldo_awal,
		})

# Delete Saldo Awal

def d_saldo_awal(req, id):
	models.SaldoAwal.objects.filter(pk=id).delete()
	return redirect('/')