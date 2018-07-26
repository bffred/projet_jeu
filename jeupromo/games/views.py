from .models import Administrator, Games , Player, Promotion, Reward, Session   
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView , UpdateView 
from .forms import PlayerForm, PromotionForm, RewardForm 


def home(request):
    return HttpResponse("""
    <h1> Bienvenue sur le projet Jeux Promotionnel ! <h1>
    """)


class GameList(ListView):
    model = Games
    template_name = 'games/games.html'

#-------------- CRUD Player --------------------

class PlayerCreate (CreateView):
    model = Player
    form_class = PlayerForm
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
    fields = '__all__'
    template_name = 'games/player-detail.html'

#-------------- CRUD Promotion --------------------

class PromotionCreate(CreateView):
    model = Promotion
    form_class = PromotionForm
    success_url = reverse_lazy('games:promotions')
    template_name = 'games/promotion-create.html'

class PromotionDetail(DetailView):
    model = Promotion
    template_name = 'games/promotion-detail.html'

class PromotionList(ListView):
    model = Promotion
    template_name = 'games/promotions.html'

class PromotionUpdate(UpdateView):
    model = Promotion
    form_class = PromotionForm
    success_url = reverse_lazy('games:promotions')
    template_name = 'games/promotion-update.html'

class PromotionDelete(DeleteView):
    model = Promotion
    success_url = reverse_lazy('games:promotions')
    template_name = 'games/promotion-delete.html'

#-------------- CRUD Reward --------------------

class RewardCreate(CreateView):
    model = Reward
    form_class = RewardForm
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
    success_url = reverse_lazy('games:rewards')
    template_name = 'games/reward-delete.html'

