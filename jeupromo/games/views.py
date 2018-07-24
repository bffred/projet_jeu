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


class playerCreate (CreateView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:playerList')

class playerUpdate (UpdateView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:playerList')

class playerDelete (DeleteView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:playerList')
    template_name = 'games/playerDelete.html'

class playerList(ListView):
    model = Player
    template_name = 'games/playerlist.html'
