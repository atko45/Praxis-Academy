from django.shortcuts import render, redirect
from . import models, forms
from datetime import timedelta
from django.utils.timezone import now


# READ Jatuh Tempo by 3 hari se

def notif_r(req):
	today = now().replace(hour=0, minute=0, second=0, microsecond=0)
	tomorrow = today + timedelta(days=10)
	
	notif = models.DataNotif.objects.filter(
		tanggal_jatuh_tempo__gte=today,
		tanggal_jatuh_tempo__lt=tomorrow,
		)
	return notif

# CREATE Notifikasi Data

def notif_c(req):
	form_input = forms.NotifForm()

	if req.POST:
		form_input = forms.NotifForm(req.POST)
		if form_input.is_valid():
			form_input.save()

	notif = models.DataNotif.objects.all()

	due = notif_r(req)

	return render(req, 'notif/notif.html',
		{
		'data': notif,
		'due': due,
		'form': form_input,
		})

# READ Notifikasi Data by id

# def notif_r(req):
# 	due_date = models.DataNotif.objects.filter(tanggal_jatuh_tempo=req.POST['tanggal_jatuh_tempo'])
# 	muncul_notif = due_date - timedelta(days=10)
	
# 	notif = models.DataNotif.objects.filter(tanggal_jatuh_tempo__lte=muncul_notif)
# 	return render(req, 'notif/notif.html',
# 		{
# 		'notif': notif,
# 		})


# Jatuh tempo harus masuk datanya.
# jatuh tempo hari ini harus muncul paling atas dan paling bawah adalah jatuh tempo terlama
# Integrasi dengan WhatsApp dalam mengingatkan notifikasi
# Analisis Kesehatan Keuangan

# UPDATE Notifikasi Data by id

def notif_u(req, id):
	if req.POST:
		models.DataNotif.objects.filter(pk=id).update(
		nama = req.POST['nama'],
		hutang = req.POST['hutang'],
		tanggal_pinjam = req.POST['tanggal_pinjam'],
		tanggal_jatuh_tempo = req.POST['tanggal_jatuh_tempo'],
		keterangan = req.POST['keterangan'],
		)
		return redirect('/')

	notif = models.DataNotif.objects.filter(pk=id).first()

	return render(req, 'notif/notif_u.html',
		{
		'data': notif,
		})

# DELETE Notifikasi Data by id

def notif_d(req, id):
	models.DataNotif.objects.filter(pk=id).delete()
	return redirect('/')