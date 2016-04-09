from django.db import models
from season.models import Player, Week
from django.conf import settings


class Game(models.Model):
    name = models.CharField(max_length=256)
    rules = models.TextField()

    def __unicode__(self):
        return self.name


class Contest(models.Model):
    game = models.ForeignKey(Game)
    week = models.OneToOneField(Week, unique=True)
    lineup_set = models.DateTimeField(blank=True, null=True)
    participants = models.ManyToManyField(Player, blank=True)

    class Meta:
        ordering = ['week']

    def __unicode__(self):
        return '%s (%s)' % (self.game, self.week)

    def __lt__(self, other):
        return self.week < other.week
