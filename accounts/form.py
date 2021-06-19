from django import forms
from django.forms import fields
from .models import User,PlayerScore,ComputerScore,RPSModel
from accounts import models

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password','contact']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = PlayerScore
        fields=['run_perball','Total_run']

class ComputerForm(forms.ModelForm):
    class Meta:
        model = ComputerScore
        fields=['run_perball','Total_run']


class RPSForm(forms.ModelForm):
    class Meta:
        model = RPSModel
        fields =['player1','player2']