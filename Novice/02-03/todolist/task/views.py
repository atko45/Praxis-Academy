from django.shortcuts import render, redirect

from . import models

#	Cara menambahkan data atau 'CREATE' data

def index(req):
	if req.POST:
		models.Task.objects.create(name=req.POST['name'])
		return redirect('/')

	tasks = models.Task.objects.all()
	return render(req, 'task/index.html',
		{ 'data': tasks,
		}) 


#	Menghubungkan dengan halaman 'detail.html' membuat 'READ'

def detail(req, id):	#Argument ke-2 harus sesuai dengan path yang ada di 'urls.py'
	task = models.Task.objects.filter(pk=id).first()
	return render(req, 'task/detail.html',
		{ 'data': task,
		}) 


#	Membuat 'Delete'

def delete(req, id):
	task = models.Task.objects.filter(pk=id).delete()
	return redirect('/')


#	Membuat 'Edit'

# def edit(req, id):
# 	task = models.Task.objects.filter(pk=id)
# 	return render(req, 'task/edit.html')