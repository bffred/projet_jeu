from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
# from . import views
from .views import *
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'games'

urlpatterns = [
    path('home', home, name = 'home'),

    path('players', PlayerList.as_view(), name='players'),
    path('', GameList.as_view(), name='games'),
    path('player-create/', PlayerCreate.as_view(), name='player-create'),
    path('player-detail/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
    path('player-update/<int:pk>/', PlayerUpdate.as_view(), name='player-update'),
    path('player-delete/<int:pk>/', PlayerDelete.as_view(), name='player-delete'),
    
    path('reward-create/', RewardCreate.as_view(), name='reward-create'),
    path('reward-detail/<int:pk>/', RewardDetail.as_view(), name='reward-detail'),
    path('rewards', RewardList.as_view(), name='rewards'),
    path('reward-update/<int:pk>/', RewardUpdate.as_view(), name='reward-update'),
    path('reward-delete/<int:pk>/', RewardDelete.as_view(), name='reward-delete'),

    path('promotion-create/', PromotionCreate.as_view(), name='promotion-create'),
    path('promotion-detail/<int:pk>', PromotionDetail.as_view(), name='promotion-detail'),
    path('promotions', PromotionList.as_view(), name='promotions'),
    path('promotion-update/<int:pk>', PromotionUpdate.as_view(), name='promotion-update'),
    path('promotion-delete/<int:pk>', PromotionDelete.as_view(), name='promotion-delete'),
    path('base', base, name='base'),
    path('test', test, name='test'),
    url(r'^login/$', login_user, name = 'login'),
    url(r'^main/$', main, name="main"),
    url(r'^signup/$', signup, name='signup'),
    url(r'logout', LogoutView.as_view(), name='logout'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)