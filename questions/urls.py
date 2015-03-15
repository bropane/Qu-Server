__author__ = 'Taylor'
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

import views


urlpatterns = patterns('',
    # Gets a random question
    url(r'^$', views.get_random_question)
    # Provide answer to question
    # url(r'^(?P<pk>\d+)/positive$', views.),
    # url(r'^(?P<pk>\d+)/negative$', views.),
)

urlpatterns = format_suffix_patterns(urlpatterns)