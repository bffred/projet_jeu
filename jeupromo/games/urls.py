from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views
from .views import gamelist2, playerDetail

app_name = 'games'

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('gamelist', views.gamelist, name='gamelist'),
    path('playerlist', views.playerlist, name='playerlist'),
    path('gamelist2', gamelist2.as_view(), name='gamelist2'),
    path('playerdetail/<int:pk>/', playerDetail.as_view(), name='playerDetail')
]