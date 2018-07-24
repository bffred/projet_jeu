from django.shortcuts import render
from .models import Games , Player , Session , Reward
from django.views.generic import TemplateView , ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy



# Create your views here.

def home(request):
    return HttpResponse("""
    <h1> Bienvenue sur le projet Jeux Promotionnel ! <h1>
    """)


class GameList2(ListView):
    model = Games
    template_name = 'games/gamelist2.html'

class PlayerCreate (CreateView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:playerList')

class PlayerUpdate (UpdateView):
    model = Player
    fields = ['pseudo'] 
    success_url = reverse_lazy('games:playerList')

class PlayerDelete (DeleteView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:playerList')
    template_name = 'games/playerDelete.html'

class PlayerList(ListView):
    model = Player
    template_name = 'games/playerlist.html'

class PlayerDetail(DetailView):
    model = Player
    fields = ['pseudo']
    template_name = 'games/playerDetail.html'