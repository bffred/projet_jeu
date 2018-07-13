from django.shortcuts import render
from .models import Games , Player , Session , Reward
from django.views.generic import TemplateView , ListView, DetailView
from django.http import HttpResponse, Http404



# Create your views here.

def view_jeux(request, id_jeux):
    return HttpResponse(
        "Le nom du jeu est : #{0} ".format(id_jeux)
    )

def home(request):
    return HttpResponse("""
    <h1> Bienvenue sur le projet Jeux Promotionnel ! <h1>
    """)