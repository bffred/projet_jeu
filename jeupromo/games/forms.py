from django.forms import ModelForm
from .models import *
from django import forms

class PlayerForm(ModelForm):
    class Meta :
        model = Player
        fields = "__all__"

class PromotionForm(ModelForm):
    class Meta:
        model = Promotion
        fields = ('name', 'administrator',)

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