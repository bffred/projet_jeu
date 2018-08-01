from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Games(models.Model):
    label = models.CharField(max_length=150, verbose_name='libellé')
    game_type = models.CharField(max_length=150, verbose_name='type de jeu')
    game_logo = models.ImageField("logo jeu", null=True, blank=True, upload_to="img/")
    description = models.TextField(max_length=150 )

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Jeu"
        verbose_name_plural = "Jeux"


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auto_increment_id = models.AutoField(primary_key=True, verbose_name = 'id')
    pseudo = models.CharField(max_length=100, verbose_name= 'pseudo', unique=True)
    name = models.CharField(max_length=50, verbose_name='nom')
    firstname = models.CharField(max_length=50, verbose_name='prénom')
    email = models.EmailField(verbose_name='email', null=True)

    def __str__(self):
        return self.pseudo

    class Meta:
        verbose_name = "Joueur"

class Administrator(Player):
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gestionnaire"

class Promotion(models.Model):
    name = models.CharField(max_length=200)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    reward = models.ManyToManyField(Games, through='PromotionGames')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Opération Promotionnelle"
        verbose_name_plural = "Opérations Promotionnelles"



class Reward(models.Model):
    label = models.CharField(max_length=150, verbose_name='libellé')
    value = models.IntegerField(verbose_name='valeur')

    def __str__(self):
        return self.label + ' ' + str(self.value)

    class Meta:
        verbose_name = "Gain"


class Session(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now())
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    result = models.CharField(max_length=150)

    def __str__(self):
        return self.player.pseudo + ' ' + self.game.label + ' ' + str(self.datetime) + ' ' + self.reward.label + ' ' + self.result

    class Meta:
        verbose_name = "Partie"

#PRG stand for Promotion Rewards Games
class PromotionGames(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Opération Promotionnelle Jeu(x) Gain(s)"
        verbose_name_plural = "Opérations Promotionnelles Jeu(x) Gain(s)"