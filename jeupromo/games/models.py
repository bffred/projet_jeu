from django.db import models

# Create your models here.
class Player(models.Model):
    pseudo = models.Charfield(verbose_name= 'pesudo', unique=True)

class Session(models.Model):
    game = models.Foreignkey(Games,on_delete=models.CASCADE)
    player = models.Foreignkey(Player,on_delete=models.CASCADE)
    datetime = models.datetime
    reward = models.Foreignkey(Reward,on_delete=models.CASCADE)
    result = models.Charfield(max_length=150)



class Reward(models.Model):
    label = models.Charfield(max_length=150)
    value = models.Integerfield(max_length=4)

class Games(models.Model):
    label = models.Charfield(max_length=150)
    game_type = models.Charfield(max_length=150)
git 