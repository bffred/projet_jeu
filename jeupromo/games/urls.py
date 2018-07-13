from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

app_name = 'games'

urlpatterns = [
    path('accueil', views.home),
]