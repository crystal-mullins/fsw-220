from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from . import views

# Create your views here.

def artist (request):
    return render(request, 'songapp/artist.html', {'artist':'Title Tag'})

def songs (request):
    return render(request, 'songapp/songs.html', {'songs':'Title Tag'})
