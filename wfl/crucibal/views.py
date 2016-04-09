from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from .models import Contest
from season.models import Result, Player, Season


def index(request):
    seasons = []
    for season in Season.objects.all():
        contests = Contest.objects.filter(week__season=season)
        if len(contests) > 0:
            seasons.append(season)
    template = loader.get_template('crucibal/index.html')
    context = RequestContext(request, {
        'seasons': seasons,
    })
    return HttpResponse(template.render(context))


def season(request, season_id):
    season = Season.objects.get(id=season_id)
    contests = Contest.objects.filter(week__season=season)
    standings = []
    for player in Player.objects.all():
        results = Result.objects.filter(entrant_id=player.id)
        results = results.filter(week__season=season)
        points = map(lambda x: x.points, results)
        standings.append((player, sum(points)))
        standings.sort(key=lambda x: x[1], reverse=True)
    template = loader.get_template('crucibal/season.html')
    context = RequestContext(request, {
        'season': season,
        'contests': contests,
        'standings': standings,
    })
    return HttpResponse(template.render(context))


def contest(request, contest_id):
    contest_obj = Contest.objects.get(id=contest_id)
    results = Result.objects.filter(week_id=contest_obj.week.id)
    template = loader.get_template('crucibal/contest.html')
    context = RequestContext(request, {
        'contest': contest_obj,
        'results': results.order_by('-points'),
    })
    return HttpResponse(template.render(context))
