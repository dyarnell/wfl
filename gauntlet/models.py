from django.db import models
from players.models import Player, Week


class VideoGame(models.Model):
    name = models.CharField(max_length=256)
    level = models.CharField(max_length=256)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.level)


class Challenge(models.Model):
    game = models.ForeignKey(VideoGame)
    week = models.OneToOneField(Week, unique=True)

    def __unicode__(self):
        return '%s (%s)' % (self.game, self.week)

    def __lt__(self, other):
        return self.week < other.week
