from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views
from .views import gamelist2, playerDetail, RewardCreate, RewardDetail, RewardList, RewardUpdate, RewardDelete

app_name = 'games'

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('gamelist', views.gamelist, name='gamelist'),
    path('playerlist', views.playerlist, name='playerlist'),
    path('gamelist2', gamelist2.as_view(), name='gamelist2'),
    path('playerdetail/<int:pk>/', playerDetail.as_view(), name='playerDetail'),
    path('reward-create', RewardCreate.as_view(), name='reward-create'),
    path('reward-detail/<int:pk>/', RewardDetail.as_view(), name='reward-detail'),
    path('reward-list', RewardList.as_view(), name='reward-list'),
    path('reward-update/<int:pk>/', RewardUpdate.as_view(), name='reward-update'),
    path('reward-delete/<int:pk>/', RewardDelete.as_view(), name='reward-delete'),
    
]