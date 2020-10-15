from django.shortcuts import render, redirect
from . import models, forms


# READ Jatuh Tempo by 3 hari se

def notif(req):
	if req.POST:
		jatuh_tempo = models.DataNotif.objects.all()
		if 	jatuh_tempo:
			models.DataNotif.objects.filter(
				due_date__gte=datetime.date(2005, 1, 1),
				pick_date_lte=datetime.date(2005, 3, 31)
				)
		jatuh_tempo = models.DataNotif.objects.all()
		return render(req, 'notif/notif.html', 
			{
			'dataa': jatuh_tempo
			})


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

# READ Notifikasi Data by id

def notif_r(req, id):
	notif = models.DataNotif.objects.filter(pk=id).first()
	return render(req, 'notif/notif_r.html',
		{
		'data': notif,
		})

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