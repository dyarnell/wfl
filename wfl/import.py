#!/usr/bin/env python

import sys
import os
import django
import fileinput
from django.core import serializers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append('%s/..' % BASE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'wfl.settings'
django.setup()

lines = []
for line in fileinput.input():
    lines.append(line)

for obj in serializers.deserialize("json", '\n'.join(lines)):
    ## remove the primary key as saving does not increment
    #sobj.object.pk = None
    print "Saving %s" % obj.object
    obj.save()
