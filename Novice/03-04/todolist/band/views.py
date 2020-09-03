from django.shortcuts import render, redirect
from . import models

#	CREATE 'daftar band'

def buat_band(req):
	if req.POST:
		models.Band.objects.create(
		nama_band=req.POST['nama_band'],
		aliran=req.POST['aliran'],
		negara_asal=req.POST['negara_asal'],
		personil=req.POST['personil'],
		posisi=req.POST['posisi'],
		status=req.POST['status']
		)
		return redirect('/')

	band = models.Band.objects.all()
	keterangan = models.Keterangan.objects.all()

	return render(req, 'daftarBand/index.html',
		{
		'data': band,
		'keterangan': keterangan,
		})

def keterangan_band(req):
	if req.POST:
		models.Keterangan.objects.create(
		tahun = req.POST['tahun'],
		label = req.POST['label']
		)
		return redirect('/')


#	READ 'daftar band'

def detail_band(req, id):
	band = models.Band.objects.filter(pk=id).first()
	return render(req, 'daftarBand/detail.html',
		{ 'data': band
		})

#	DELETE 'daftar band'

def delete_data(req, id):
	models.Band.objects.filter(pk=id).delete()
	return redirect('/')

def delete_keterangan(req, id):
	models.Keterangan.objects.filter(pk=id).delete()
	return redirect('/')

#	UPGRADE	'daftar band'

def upgrade_data(req, id):
	if req.POST:
		models.Band.objects.filter(pk=id).update(
		nama_band=req.POST['nama_band'],
		aliran=req.POST['aliran'],
		negara_asal=req.POST['negara_asal'],
		personil=req.POST['personil'],
		posisi=req.POST['posisi'],
		status=req.POST['status']
		)
		return redirect('/')

	bands = models.Band.objects.filter(pk=id).first()
	return render(req, 'daftarBand/upgrade.html',
		{ 'data': bands,
		})