from django.db import models
from season.models import Player, Week
from django.conf import settings
import math
from season.notify import email_week, email_post


def largest_power(i, power=2):
    start = 0
    while True:
        if int(math.pow(power, start)) > i:
            return int(math.pow(power, start-1))
        else:
            start += 1


class VideoGame(models.Model):
    name = models.CharField(max_length=256)
    level = models.CharField(max_length=256)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.level)


class Challenge(models.Model):
    game = models.ForeignKey(VideoGame)
    week = models.OneToOneField(Week, unique=True)
    lineup_set = models.DateTimeField(blank=True, null=True)
    participants = models.ManyToManyField(Player, blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.game, self.week)

    def __lt__(self, other):
        return self.week < other.week

    def send_mail(self):
        emails = set(map(lambda x: x.user.email, Player.objects.all()))
        for email in emails:
            players = map(lambda x: str(x),
                          Player.objects.filter(user__email=email))
            date_string = self.week.kickoff.strftime('%B %d, %Y at %I:%M %p')
            message = email_week % (self.week.week, self.week.season,
                                    date_string, ', '.join(players),
                                    settings.WFL_URL)
            self.week.send_mail(email, settings.WFL_ADMIN,
                                message + email_post)
        self.week.notified = True
        self.week.save()


class BracketMatch(models.Model):
    challenge = models.ForeignKey(Challenge)
    player1 = models.ForeignKey(Player, blank=True, related_name='player1')
    player2 = models.ForeignKey(Player, blank=True, related_name='player2')
    round = models.IntegerField()
