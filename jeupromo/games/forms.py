from django.forms import ModelForm, TextInput, DateInput
from .models import *


class PlayerForm(ModelForm):
    class Meta :
        model = Player
        fields = ['pseudo']

class PromotionForm(ModelForm):
    class Meta:
        model = Promotion
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'date_start': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_end': DateInput(attrs={'type': 'date','class': 'form-control'}),
            'administrator': TextInput(attrs={'class': 'form-control'}),
            
        }

class RewardForm(ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"