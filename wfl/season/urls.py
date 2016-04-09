from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^players/$', views.players, name='players'),
    url(r'^$', views.list, name='list'),
    url(r'^(?P<season_id>[0-9]+)/$', views.season),
    url(r'^(?P<season_id>[0-9]+)/week/(?P<week_id>[0-9]+?)/$', views.week),
    url(r'^[0-9]/week/(?P<week_id>[0-9]+?)/result/$',
        views.result),
    url(r'^[0-9]/week/(?P<week_id>[0-9]+?)/email/$',
        views.email),
    url(r'^sendmail/$', views.sendmail, name='sendmail'),
]
