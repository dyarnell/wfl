from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^season/(?P<season_id>\d+)/$', views.season, name='season'),
    url(r'^challenge/(?P<challenge>\d+)/$', views.challenge, name='challenge')
]
