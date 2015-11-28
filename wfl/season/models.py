from django.db import models
from django.contrib.auth.models import User
import datetime


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

    def __unicode__(self):
        return '%s - Week %d' % (self.season, self.week)

    def __lt__(self, other):
        if self.season == other.season:
            return self.week < other.week
        else:
            return self.season < other.season


class Result(models.Model):
    entrant = models.ForeignKey(Player)
    points = models.IntegerField()
    week = models.ForeignKey(Week)

    class Meta:
        verbose_name_plural = 'Results'

    def __unicode__(self):
        return '%s %s' % (self.entrant, self.week)