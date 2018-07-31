from django.forms import ModelForm, TextInput, DateInput
from .models import *
from django import forms


class PlayerForm(ModelForm):
    class Meta :
        model = Player
        fields = "__all__"

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

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class LogoutForm(forms.Form):
    pass

class UserForm(ModelForm):
    class Meta :
        model = User
        fields = '__all__'