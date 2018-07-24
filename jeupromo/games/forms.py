from django.forms import ModelForm
from .models import *

class playerForm(ModelForm):
    class Meta :
        model = Player
        fields = ['pseudo']
        