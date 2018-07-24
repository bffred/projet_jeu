from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views
from .views import GameList2, PlayerDetail, PlayerCreate, PlayerDelete, PlayerUpdate, PlayerList

app_name = 'games'

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('player-list', PlayerList.as_view(), name='playerList'),
    path('game-list', GameList2.as_view(), name='gamelist'),
    path('player-detail/<int:pk>/', PlayerDetail.as_view(), name='playerDetail'),
    path('player-update/<int:pk>/', PlayerUpdate.as_view(), name='playerUpdate'),
    path('player-delete/<int:pk>/', PlayerDelete.as_view(), name='playerDelete'),
    path('player-create/', PlayerCreate.as_view(), name='playerCreate')
]