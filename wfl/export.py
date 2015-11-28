#!/usr/bin/env python

import sys
import os
import django
from django.core import serializers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'wfl.settings'
django.setup()

from django.contrib.auth.models import User
from season.models import Player, Season, Week, Result
from gauntlet.models import VideoGame, Challenge, BracketMatch

models = [User, Player, Season, Week, Result, VideoGame, Challenge,
          BracketMatch]

serialzed_objects = []
for model in models:
    objs = model.objects.all()
    if objs:
        serialzed_objects += objs
print serializers.serialize('json', serialzed_objects)
