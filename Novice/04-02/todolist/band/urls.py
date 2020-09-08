"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.index),

    path('genre', views.buat_genre),
    path('band/', views.buat_band),

    path('<id>/detail-genre', views.detail_genre),
    path('<id>/update-genre', views.update_genre),
    path('<id>/delete-genre', views.delete_genre),

    path('<id>/detail-band', views.detail_band),
    path('<id>/update-band', views.update_band),
    path('<id>/delete-band', views.delete_band),
]
