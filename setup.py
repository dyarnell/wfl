#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='wfl',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='Wood Foot League',
    # GETTING-STARTED: set author name (your name):
    author='Derek Yarnell',
    # GETTING-STARTED: set author email (your email):
    author_email='derektyarnell@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.11',
        'django-widget-tweaks==1.3',
        'django-bootstrap3-datetimepicker==2.2.3',
        'django-bootstrap3>=6.2.2',
	'pytz==2015.7',
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
