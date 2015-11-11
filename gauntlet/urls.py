from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^challenge/(?P<challenge>\d+)/$', views.challenge, name='challenge')
]
