from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('about', views.about),
    path('experience', views.experience),
    path('portfolio', views.portfolio),
    path('services', views.services),
    path('contact', views.contact),
]