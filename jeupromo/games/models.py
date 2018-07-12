from django.db import models

# Create your models here.
class Player(models.Model):
    pseudo = models.CharField(max_length=100, verbose_name= 'pseudo', unique=True)

class Reward(models.Model):
    label = models.CharField(max_length=150)
    value = models.IntegerField()

class Games(models.Model):
    label = models.CharField(max_length=150)
    game_type = models.CharField(max_length=150)

class Session(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    result = models.CharField(max_length=150)



