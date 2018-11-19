# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from . import views


app_name = 'like'
urlpatterns = [
#   url(r'^(?P<comment_id>\d+)/(?P<five_stars>[1-5]{1})/create/$', views.create, name='create'),
    url(r'^(?P<comment_id>\d+)/(?P<five_stars>[1-5]{1})/update/$', views.update, name='update'),
#   url(r'^(?P<pk>\d+)/delete/$', views.delete, name='delete'),

]
