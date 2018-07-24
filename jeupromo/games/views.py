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

def gamelist(request):
    games = Games.objects.all()
    return render(request, 'games/affichageJeux.html', {'games':games})

def playerlist(request):
    players = Player.objects.all()
    return render(request, 'games/playerlist.html', {'players':players})


class gamelist2(ListView):
    model = Games
    template_name = 'games/gamelist2.html'

class playerDetail(DetailView):
    context_object_name = 'player'
    queryset = Player.objects.all()
    template_name = 'game/playerDetail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['players'] = Player.objects.all()
        return context

class RewardCreate(CreateView):
    model = Reward
    fields = ['label', 'value']
    #form_class = RewardForm
    success_url = reverse_lazy('games:reward-list')
    template_name = 'games/reward-create.html'

class RewardDetail(DetailView):
    model = Reward
    template_name = 'games/reward-detail.html'

class RewardList(ListView):
    model = Reward
    template_name = 'games/reward-list.html'

class RewardUpdate(UpdateView):
    model = Reward
    form_class = RewardForm
    success_url = reverse_lazy('games:reward-list')
    template_name = 'games/reward-update.html'

class RewardDelete(DeleteView):
    model = Reward
    form_class = RewardForm
    success_url = reverse_lazy('games:reward-list')
    template_name = 'games/reward-delete.html'


    
