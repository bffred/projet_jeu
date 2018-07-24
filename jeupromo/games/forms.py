from django import forms
from .models import *

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"