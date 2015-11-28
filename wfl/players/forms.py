from django import forms
from django.contrib.auth.models import User
from players.models import Player, Season


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['birthday']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class SeasonForm(forms.ModelForm):
    weeks = forms.IntegerField()

    class Meta:
        model = Season
        fields = ['season', 'year']
