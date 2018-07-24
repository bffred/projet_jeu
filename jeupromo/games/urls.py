from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views
from .views import GameList, PlayerDetail, PlayerCreate, PlayerDelete, PlayerUpdate, PlayerList

app_name = 'games'

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('players', PlayerList.as_view(), name='players-list'),
    path('', GameList.as_view(), name='games-list'),
    path('players-detail/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
    path('players-update/<int:pk>/', PlayerUpdate.as_view(), name='player-update'),
    path('players-delete/<int:pk>/', PlayerDelete.as_view(), name='player-delete'),
    path('players-create/', PlayerCreate.as_view(), name='player-create')
]