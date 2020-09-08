from django.shortcuts import render, redirect
from . import models, forms



def buat_label(req):
	form_input = forms.StudiosForm()

	if req.POST:
		form_input = forms.StudiosForm(req.POST)
		if form_input.is_valid():
			form_input.save()

	studio = models.Studios.objects.all()

	return render(req, 'studio/studio.html',
		{
		'studio': studio,
		'form': form_input,
		})



def baca_label(req, id):
	studio = models.Studios.objects.filter(pk=id).first()
	return render(req, 'studio/studio_r.html',
		{ 
		'studio': studio
		})



def delete_label(req, id):
	models.Studios.objects.filter(pk=id).delete()
	return redirect('/studio')



def update_label(req, id):
	if req.POST:
		models.Studios.objects.filter(pk=id).update(
		nama_label=req.POST['n_label'],
		tahun_berdiri=req.POST['t_berdiri'],
		status_label=req.POST['s_label'],
		negara_label=req.POST['ne_label']
		)
		return redirect('/studio')

	studios = models.Studios.objects.filter(pk=id).first()
	return render(req, 'studio/studio_u.html',
		{ 'studio': studios,
		})