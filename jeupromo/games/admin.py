from django.contrib import admin
from .models import *

class PlayerAdmin (admin.ModelAdmin):
    list_display = ('pseudo', 'name', 'firstname', 'email',)
    ordering = ('name',)
    search_fields =('name', 'firstname',)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('label', 'value',)
    lsit_filter = ('label',)

# #A utiliser Lorsqu'il y a une ForeignKey dans la table 
# class RewardInline(admin.TabularInline):
#     model = Reward
#     fieldsets  = [
#         (None, {'fields': ['label', 'value']})
#     ]

# @admin.register(Reward)
# class RewardAdmin (admin.ModelAdmin):
#     inlines = [RewardInline,]
#     # list_display = ('label', 'value')          #Liste des champs du modèle à afficher dans le Tableau
#     # list_filter = ('label',)                    #Liste des champs à partir desquels nous pourrons filtrer les entrées
#     # date_hierarchy = ('date_start',)            #Permet de filtrer par date de façon intuitive
#     # ordering = ('label',)                       #Tri par defaut du tableau
#     # search_fields = ('label',)                  #Configuration du champs recherche

@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Games)
class GamesAdmin (admin.ModelAdmin):
    list_display = ('label', 'game_type')
    list_filter = ('game_type',)
    search_fields = ('label',)

class SessionAdmin (admin.ModelAdmin):
    list_display = ('game', 'player', 'datetime', 'reward', 'result')
    date_hierarchy = ('datetime')
    list_filter = ('game',)

class PromotionAdmin(admin.ModelAdmin):
    date_hierarchy = ('date_start',)
    search_fields = ('date_start', 'name',)

admin.site.register(Reward, RewardAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Promotion)
# admin.site.register(Game)
# admin.site.register(Administrator, AdministratorAdmin)