from django import forms
from django.contrib.auth.models import User
from .models import Player, Season, Week, Result
from bootstrap3_datetime.widgets import DateTimePicker


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


class SeasonPlayerForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['players']


class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        fields = ['season', 'kickoff', 'duration']
        widgets = {
            'kickoff': DateTimePicker(options={"format": "YYYY-MM-DD"}),
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['entrant', 'points']
