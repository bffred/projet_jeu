from django.shortcuts import render
from .models import Games , Player , Session , Reward
from django.views.generic import TemplateView , ListView, DetailView
from django.http import HttpResponse, Http404



# Create your views here.

def home(request):
    return HttpResponse("""
    <h1> Bienvenue sur le projet Jeux Promotionnel ! <h1>
    """)

def gamelist(request):
    games = Games.objects.all()
    return render(request, 'games/affichageJeux.html', {'games':games})
