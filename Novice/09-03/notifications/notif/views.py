from django.shortcuts import render, redirect
from . import models, forms
# CREATE Notifikasi Data

def notif_c(req):
	form_input = forms.NotifForm()

	if req.POST:
		form_input = forms.NotifForm(req.POST)
		if form_input.is_valid():
			form_input.save()

	notif = models.DataNotif.objects.all()

	return render(req, 'notif/notif.html',
		{
		'data': notif,
		'form': form_input,
		})


def notif_r(req, id):
	notif = models.DataNotif.objects.filter(pk=id).first()
	return render(req, 'notif/notif_r.html',
		{
		'data': notif,
		})

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

def notif_d(req, id):
	models.DataNotif.objects.filter(pk=id).delete()
	return redirect('/')