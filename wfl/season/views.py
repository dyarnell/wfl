from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

from .models import Season, Week, Player, Result
from .forms import UserForm, PlayerForm, SeasonForm, WeekForm, ResultForm, \
    SeasonPlayerForm, EmailForm
from .notify import rules_list


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


def list(request):
    ctx = {}
    ctx['seasons'] = Season.objects.all()
    ctx['rules'] = rules_list
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


def season(request, season_id):
    ctx = {}
    ctx['season'] = Season.objects.get(pk=season_id)
    ctx['weeks'] = Week.objects.filter(season=season_id)
    ctx['sp_form'] = SeasonPlayerForm(instance=ctx['season'])
    if request.method == 'POST':
        sp_form = SeasonPlayerForm(request.POST, instance=ctx['season'])
        if sp_form.is_valid():
            sp_form.save()
            messages.success(request, 'Updated %s' % ctx['season'])
            ctx['sp_form'] = SeasonPlayerForm(instance=ctx['season'])
    template = loader.get_template('season/season.html')
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))


def week(request, season_id, week_id):
    ctx = {}
    week = Week.objects.get(pk=week_id)
    if request.method == 'POST':
        week_form = WeekForm(request.POST)
        if week_form.is_valid():
            update_week = week_form.save(commit=False)
            week.season = update_week.season
            week.duration = update_week.duration
            week.kickoff = update_week.kickoff
            week.save()
            messages.success(request, 'Updated %s' % week)
            week_form = WeekForm(instance=Week.objects.get(pk=week_id))
    else:
        week_form = WeekForm(instance=week)
    ctx['result_form'] = ResultForm()
    ctx['week_form'] = week_form
    ctx['week'] = week
    ctx['results'] = Result.objects.filter(week=week_id)
    template = loader.get_template('season/week.html')
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))


def result(request, week_id):
    week = Week.objects.get(pk=week_id)
    if request.method == 'POST':
        result_form = ResultForm(request.POST)
        if result_form.is_valid():
            result = result_form.save(commit=False)
            result.week = week
            try:
                result.save()
                messages.success(request, 'Added result %s for Week %s.' %
                                 (result, week))
            except:
                messages.error(request, 'Unable to add result.')
            return redirect(request.GET['next'])


def sendmail(request):
    ctx = {}
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            subject = email_form.cleaned_data['subject']
            body = email_form.cleaned_data['body']
            send_mail(subject, body, settings.WFL_ADMIN,
                      ['derek@umiacs.umd.edu'], fail_silently=False)
            email_form = EmailForm()
    else:
        email_form = EmailForm()
    ctx['email_form'] = email_form
    template = loader.get_template('season/sendmail.html')
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))
