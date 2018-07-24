from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views
from .views import GameList2, PlayerDetail, PlayerCreate, PlayerDelete, PlayerUpdate, PlayerList

app_name = 'games'

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('playerlist', PlayerList.as_view(), name='playerList'),
    path('gamelist', GameList2.as_view(), name='gamelist'),
    path('playerdetail/<int:pk>/', PlayerDetail.as_view(), name='playerDetail'),
    path('playerupdate/<int:pk>/', PlayerUpdate.as_view(), name='playerUpdate'),
    path('playerdelete/<int:pk>/', PlayerDelete.as_view(), name='playerDelete'),
    path('playercreate/', PlayerCreate.as_view(), name='playerCreate')
]