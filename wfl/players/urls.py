from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^create/season/$', views.create_season, name='create_season')
]
