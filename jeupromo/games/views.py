from django.shortcuts import render
from .models import Games , Player , Session , Reward, Administrator
from django.views.generic import TemplateView , ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from .forms import RewardForm
from django.urls import reverse_lazy




# Create your views here.

def home(request):
    return HttpResponse("""
    <h1> Bienvenue sur le projet Jeux Promotionnel ! <h1>
    """)

def base(request):
    return render(request, 'games/base.html')


class GameList(ListView):
    model = Games
    template_name = 'games/games-list.html'

class PlayerCreate (CreateView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:players')

class PlayerUpdate (UpdateView):
    model = Player
    fields = ['pseudo'] 
    success_url = reverse_lazy('games:players')

class PlayerDelete (DeleteView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:players')
    template_name = 'games/player-delete.html'

class PlayerList(ListView):
    model = Player
    template_name = 'games/players.html'

class PlayerDetail(DetailView):
    model = Player
    fields = ['pseudo']
    template_name = 'games/player-detail.html'


class RewardCreate(CreateView):
    model = Reward
    fields = ['label', 'value']
    #form_class = RewardForm
    success_url = reverse_lazy('games:rewards')
    template_name = 'games/reward-create.html'

class RewardDetail(DetailView):
    model = Reward
    template_name = 'games/reward-detail.html'

class RewardList(ListView):
    model = Reward
    template_name = 'games/rewards.html'

class RewardUpdate(UpdateView):
    model = Reward
    form_class = RewardForm
    success_url = reverse_lazy('games:rewards')
    template_name = 'games/reward-update.html'

class RewardDelete(DeleteView):
    model = Reward
    form_class = RewardForm
    success_url = reverse_lazy('games:rewards')
    template_name = 'games/reward-delete.html'


    
