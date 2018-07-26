from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views
from .views import GameList, PlayerDetail, PlayerCreate, PlayerDelete, PlayerUpdate, PlayerList, RewardCreate, RewardDetail, RewardList, RewardUpdate, RewardDelete

app_name = 'games'

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('players', PlayerList.as_view(), name='players'),
    path('', GameList.as_view(), name='games-list'),
    path('player-detail/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
    path('player-update/<int:pk>/', PlayerUpdate.as_view(), name='player-update'),
    path('player-delete/<int:pk>/', PlayerDelete.as_view(), name='player-delete'),
    path('player-create/', PlayerCreate.as_view(), name='player-create'),
    
    path('reward-create', RewardCreate.as_view(), name='reward-create'),
    path('reward-detail/<int:pk>/', RewardDetail.as_view(), name='reward-detail'),
    path('rewards', RewardList.as_view(), name='rewards'),
    path('reward-update/<int:pk>/', RewardUpdate.as_view(), name='reward-update'),
    path('reward-delete/<int:pk>/', RewardDelete.as_view(), name='reward-delete'),

    path('base', views.base, name='base'),
    
]