from django.forms import ModelForm
from .models import *

class playerForm(ModelForm):
    class Meta :
        model = Player
        fields = ['pseudo']
        


class RewardForm(ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"
