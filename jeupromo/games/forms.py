from django.forms import ModelForm, FileInput, EmailInput, TextInput, DateInput
from .models import *

class PlayerForm(ModelForm):
    class Meta :
        model = Player
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'type':"text", 
                'id':"LastName",
                'name':"LastName",
                'placeholder':"Nom",
                'class':"input-xlarge"
                              }),
            'firstname': TextInput(attrs={
                'type':"text", 
                'id':"FirstName",
                'name':"FirstName",
                'placeholder':"Prénom",
                'class':"input-xlarge"
                              }),
            'email': EmailInput(attrs={
                'type':"email", 
                'id':"email",
                'name':"email",
                'placeholder':"Adresse E-mail",
                'class':"input-xlarge"
                              }),
            'dateNaissance': DateInput(attrs={
                'type':"date", 
                'id':"dateNaissance",
                'name':"dateNaissance",
                'placeholder':"Date de Naissance",
                'class':"input-xlarge"
                              }),
            'pseudo': TextInput(attrs={
                'type':"text", 
                'id':"Pseudo",
                'name':"Pseudo",
                'placeholder':"Pseudo",
                'class':"input-xlarge"
                              }),
            # 'img_player': FileInput(attrs={
            #     'type':"file", 
            #     'name':"LastName",
            #     'placeholder':"Nom",
            #     'class':"btn btn-outline-primary"
            #                   }),
            
        }

class PromotionForm(ModelForm):
    class Meta:
        model = Promotion
        fields = ('name', 'administrator',)

class RewardForm(ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"