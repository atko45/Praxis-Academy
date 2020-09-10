from django.shortcuts import render, redirect
from . import models, forms


def create_elektronik(req):
	form_input = forms.ElektronikForm()

	if req.POST:
		form_input = forms.ElektronikForm(req.POST)
		if form_input.is_valid():
			form_input.save()

	electro = models.Elektronik.objects.all()

	return render(req, 'elektronik_t/elektronik_h.html',
		{
		'electro': electro,
		'form': form_input,
		})

def read_elektronik(req, id):
	electro = models.Elektronik.objects.filter(pk=id).first()
	return render(req, 'elektronik_t/elektronik_r.html',
		{ 
		'electro': electro
		})



def delete_elektronik(req, id):
	models.Elektronik.objects.filter(pk=id).delete()
	return redirect('/')



def update_elektronik(req, id):
	if req.POST:
		models.Elektronik.objects.filter(pk=id).update(
		elek_image = req.POST['gambar'],
		elek_name = req.POST['nama'],
		elek_stock = req.POST['stok'],
		elek_price = req.POST['harga'],
		elek_info = req.POST['keterangan'],
		)
		return redirect('/')

	electro = models.Elektronik.objects.filter(pk=id).first()
	return render(req, 'elektronik_t/elektronik_u.html',
		{ 'electro': electro,
		})