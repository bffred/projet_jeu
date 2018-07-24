from django.shortcuts import render
from .models import Games , Player , Session , Reward, Administrator
from django.views.generic import TemplateView , ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy



# Create your views here.

def home(request):
    return HttpResponse("""
    <h1> Bienvenue sur le projet Jeux Promotionnel ! <h1>
    """)


class GameList(ListView):
    model = Games
    template_name = 'games/games-list.html'

class PlayerCreate (CreateView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:players-list')

class PlayerUpdate (UpdateView):
    model = Player
    fields = ['pseudo'] 
    success_url = reverse_lazy('games:players-list')

class PlayerDelete (DeleteView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:players-list')
    template_name = 'games/player-delete.html'

class PlayerList(ListView):
    model = Player
    template_name = 'games/players-list.html'

class PlayerDetail(DetailView):
    model = Player
    fields = ['pseudo']
    template_name = 'games/player-detail.html'