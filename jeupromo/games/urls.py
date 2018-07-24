from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views
from .views import gamelist2, playerDetail, playerCreate, playerDelete, playerUpdate, playerList

app_name = 'games'

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('playerlist', playerList.as_view(), name='playerList'),
    path('gamelist', gamelist2.as_view(), name='gamelist'),
    path('playerdetail/<int:pk>/', playerDetail.as_view(), name='playerDetail'),
    path('playerupdate/<int:pk>/', playerUpdate.as_view(), name='playerUpdate'),
    path('playerdelete/<int:pk>/', playerDelete.as_view(), name='playerDelete'),
    path('playercreate/', playerCreate.as_view(), name='playerCreate')
]