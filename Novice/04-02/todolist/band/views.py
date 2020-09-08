from django.shortcuts import render, redirect
from . import models, forms

def index(req):
	return render(req, 'daftarBand/index.html')


#	CREATE 'daftar band'

def buat_genre(req):
	form_input = forms.GenreForm()

	if req.POST:
		form_input = forms.GenreForm(req.POST)
		if form_input.is_valid():
			form_input.save()

	genre = models.Genre.objects.all()

	return render(req, 'daftarBand/genre.html',
		{
		'genre': genre,
		'form': form_input,
		})

def buat_band(req):
	form_input = forms.BandForm()

	if req.POST:
		form_input = forms.BandForm(req.POST)
		if form_input.is_valid():
			form_input.save()

	band = models.Band.objects.all()

	return render(req, 'daftarBand/band.html',
		{
		'band': band,
		'form': form_input,
		})




#	READ 'daftar band'

def detail_genre(req, id):
	genre = models.Genre.objects.filter(pk=id).first()
	return render(req, 'daftarBand/genre_r.html',
		{ 'genre': genre
		})


def detail_band(req, id):
	band = models.Band.objects.filter(pk=id).first()
	return render(req, 'daftarBand/band_r.html',
		{ 'band': band
		})



#	DELETE 'daftar band'

def delete_genre(req, id):
	models.Genre.objects.filter(pk=id).delete()
	return redirect('/genre')

def delete_band(req, id):
	models.Band.objects.filter(pk=id).delete()
	return redirect('/band')



#	UPDATE	'daftar band'

def update_genre(req, id):
	if req.POST:
		models.Genre.objects.filter(pk=id).update(
		genre=req.POST['genre'],
		tahun=req.POST['tahun'],
		negara_asal=req.POST['negara_asal'],
		)
		return redirect('/genre')

	genres = models.Genre.objects.filter(pk=id).first()
	return render(req, 'daftarBand/genre_u.html',
		{ 'genre': genres,
		})


def update_band(req, id):
	if req.POST:
		models.Band.objects.filter(pk=id).update(
		nama_band=req.POST['nama_band'],
		aliran=req.POST['aliran'],
		negara_asal=req.POST['negara_asal'],
		tahun=req.POST['tahun'],
		label=req.POST['label'],
		status=req.POST['status']
		)
		return redirect('/band')

	bands = models.Band.objects.filter(pk=id).first()
	return render(req, 'daftarBand/band_u.html',
		{ 'band': bands,
		})