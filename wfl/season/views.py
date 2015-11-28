from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Season, Week, Player
from .forms import UserForm, PlayerForm, SeasonForm


@login_required()
def players(request):
    ctx = {}
    ctx['players'] = Player.objects.all()
    if request.method == 'POST':
        player_form = PlayerForm(request.POST)
        user_form = UserForm(request.POST)
        if all((player_form.is_valid(), user_form.is_valid())):
            user = user_form.save()
            player = player_form.save(commit=False)
            player.user = user
            player.save()
            messages.success(request, 'Player %s created.' % player)
            # reset the forms
            player_form = PlayerForm()
            user_form = UserForm()
    else:
        player_form = PlayerForm()
        user_form = UserForm()
    ctx['player_form'] = player_form
    ctx['user_form'] = user_form
    template = loader.get_template('season/players.html')
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))


@login_required()
def list(request):
    ctx = {}
    ctx['seasons'] = Season.objects.all()
    if request.method == 'POST':
        season_form = SeasonForm(request.POST)
        if season_form.is_valid():
            season = season_form.save()
            for x in range(season_form.cleaned_data['weeks']):
                week = Week.objects.create(season=season, week=x+1)
                week.save()
            messages.success(request, 'Season %s created with %d weeks.' %
                             (season, season_form.cleaned_data['weeks']))
            season_form = SeasonForm()
    else:
        season_form = SeasonForm()
    ctx['season_form'] = season_form
    template = loader.get_template('season/seasons.html')
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))
