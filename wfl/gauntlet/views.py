from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from .models import Challenge
from season.models import Result, Player, Season


def index(request):
    seasons = []
    for season in Season.objects.all():
        challenges = Challenge.objects.filter(week__season=season)
        if len(challenges) > 0:
            seasons.append(season)
    template = loader.get_template('gauntlet/index.html')
    context = RequestContext(request, {
        'seasons': seasons,
    })
    return HttpResponse(template.render(context))


def season(request, season_id):
    season = Season.objects.get(id=season_id)
    challenges = Challenge.objects.filter(week__season=season)
    standings = []
    for player in Player.objects.all():
        results = Result.objects.filter(entrant_id=player.id)
        results = results.filter(week__season=season)
        points = map(lambda x: x.points, results)
        standings.append((player, sum(points)))
        standings.sort(key=lambda x: x[1], reverse=True)
    template = loader.get_template('gauntlet/season.html')
    context = RequestContext(request, {
        'season': season,
        'challenges': challenges,
        'standings': standings,
    })
    return HttpResponse(template.render(context))


def challenge(request, challenge):
    challenge_obj = Challenge.objects.get(id=challenge)
    results = Result.objects.filter(week_id=challenge_obj.week.id)
    template = loader.get_template('gauntlet/challenge.html')
    context = RequestContext(request, {
        'challenge': challenge_obj,
        'results': results.order_by('-points'),
    })
    return HttpResponse(template.render(context))
