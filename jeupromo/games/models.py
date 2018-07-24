from django.db import models
from django.utils import timezone

# Create your models here.
class Player(models.Model):
    pseudo = models.CharField(max_length=100, verbose_name= 'pseudo', unique=True)

    def __str__(self):
        return self.pseudo

    class Meta:
        verbose_name = "Joueur"

class Reward(models.Model):
    label = models.CharField(max_length=150)
    value = models.IntegerField()

    def __str__(self):
        return self.label + ' ' + str(self.value)

    class Meta:
        verbose_name = "Gain"

class Games(models.Model):
    label = models.CharField(max_length=150)
    game_type = models.CharField(max_length=150)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Jeux"


class Session(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now())
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    result = models.CharField(max_length=150)

    def __str__(self):
        return self.player.pseudo + ' ' + self.game.label + ' ' + str(self.datetime) + ' ' + self.reward.label + ' ' + self.result

    class Meta:
        verbose_name = "Session"

class Administrator(models.Model):
    name = models.CharField(max_length=150)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gestionnaire"

