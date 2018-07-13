from django.contrib import admin
from .models import *


class RewardAdmin (admin.ModelAdmin):
    # list_display = ('label', 'value')
    search_fields = ('label')

class GamesAdmin (admin.ModelAdmin):
    # list_display = ('label', 'game_type')
    list_filter = ('game_type')
    search_fields = ('label')

class SessionAdmin (admin.ModelAdmin):
    # list_display = ('game', 'player', 'datetime', 'reward', 'result')
    date_hierarchy = ('datetime')
    list_filter = ('game')

class PlayerAdmin (admin.ModelAdmin):
    pass

admin.site.register(Reward)
admin.site.register(Games)
admin.site.register(Session)
admin.site.register(Player)