from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import datetime
import pytz
import textwrap
from django.utils import timezone
from season.notify import email_week, email_post


class Player(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()

    class Meta:
        verbose_name_plural = "Players"

    def __unicode__(self):
        if self.user.first_name and self.user.last_name:
            return '%s %s.' % (self.user.first_name, self.user.last_name[0])
        else:
            return self.user

    @property
    def age(self):
        now = datetime.datetime.now().date()
        return (now - self.birthday).days / 365

    @staticmethod
    def emails(players=None):
        if players is None:
            email_set = set(map(lambda x: x.user.email, Player.objects.all()))
        else:
            email_set = set(map(lambda x: x.user.email, players))
        if None in email_set:
            email_set.remove(None)
        return email_set


class Location(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Season(models.Model):
    SEASONS = (
        (0, 'Spring'),
        (1, 'Summer'),
        (2, 'Fall'),
        (3, 'Winter'),
    )

    season = models.IntegerField(choices=SEASONS)
    year = models.DateField()
    players = models.ManyToManyField(Player, blank=True)
    completed = models.BooleanField()

    class Meta:
        ordering = ['-season']

    def __unicode__(self):
        return '%s %d' % (self.season_title, self.year.year)

    def __lt__(self, other):
        if self.year == other.year:
            return self.season < other.season
        else:
            return self.year < other.year

    @property
    def season_title(self):
        return self.SEASONS[self.season][1]


class Week(models.Model):
    season = models.ForeignKey(Season)
    week = models.IntegerField()
    kickoff = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    notified = models.BooleanField(default=False)
    location = models.ForeignKey(Location)

    class Meta:
        ordering = ['week']
        unique_together = ('season', 'week')

    def __unicode__(self):
        return '%s - Week %d' % (self.season, self.week)

    def __lt__(self, other):
        if self.season == other.season:
            return self.week < other.week
        else:
            return self.season < other.season

    @property
    def has_passed(self):
        return (self.kickoff + self.duration) < timezone.now()

    def _send_mail(self, email_to, email_from, message, subject=None):
        if subject is None:
            subject = 'Wood Foot League Week %d Season %s' % \
                (self.week, self.season)
        if type(email_to) is not list:
            email_to = [email_to]
        if not self.notified:
            send_mail(subject, message, email_from, email_to,
                      fail_silently=False)

    def send_mail(self, email_post):
        for email in Player.emails(self.season.players.all()):
            players = map(lambda x: str(x),
                          self.season.players.filter(user__email=email))
            local_dt = self.kickoff.replace(tzinfo=pytz.utc)
            local_dt = local_dt.astimezone(pytz.timezone("America/New_York"))
            date_string = local_dt.strftime('%B %d, %Y at %I:%M %p %Z')
            message = email_week % (self.week, self.season,
                                    date_string, self.location,
                                    ', '.join(players), settings.WFL_URL)
            self._send_mail(
                email, settings.WFL_ADMIN,
                message + '\n' + '\n'.join(textwrap.wrap(email_post, 79))
            )
        self.notified = True
        self.save()


class Result(models.Model):
    entrant = models.ForeignKey(Player)
    points = models.IntegerField()
    week = models.ForeignKey(Week)

    class Meta:
        verbose_name_plural = 'Results'
        unique_together = ('entrant', 'week')

    def __unicode__(self):
        return '%s %s' % (self.entrant, self.week)
