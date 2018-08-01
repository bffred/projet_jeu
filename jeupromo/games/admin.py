from django.contrib import admin
from .models import *

@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Games)
class GamesAdmin (admin.ModelAdmin):
    list_display = ('label', 'game_type', 'description','game_logo' )
    list_filter = ('game_type',)
    search_fields = ('label',)

class PlayerAdmin (admin.ModelAdmin):
    list_display = ('pseudo', 'name', 'firstname', 'email',)
    ordering = ('name',)
    search_fields =('name', 'firstname',)

class PromotionAdmin(admin.ModelAdmin):
    date_hierarchy = ('date_start',)
    search_fields = ('date_start', 'name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Date', {
            'fields': ('date_start', 'date_end')
        }),
    )

class RewardAdmin(admin.ModelAdmin):
    list_display = ('label', 'value',)
    lsit_filter = ('label',)

class SessionAdmin (admin.ModelAdmin):
    list_display = ('game', 'player', 'datetime', 'reward', 'result')
    date_hierarchy = ('datetime')
    list_filter = ('game',)


admin.site.register(Reward, RewardAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Promotion)
admin.site.register(PromotionGames)