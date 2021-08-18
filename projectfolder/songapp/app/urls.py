from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    
    path('artist/', views.artist, name="songapp-artist"), 
    # // add more paths for additional pages
    path('about/', views.about, name="songapp-about"),
 
]
