from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Challenge
from players.models import Result, Player


def index(request):
    challenges = Challenge.objects.all()
    standings = []
    for player in Player.objects.all():
        points = map(lambda x: x.points,
                     Result.objects.filter(entrant_id=player.id))
        standings.append((player, sum(points)))
    template = loader.get_template('gauntlet/index.html')
    context = RequestContext(request, {
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
        'results': results,
    })
    return HttpResponse(template.render(context))
