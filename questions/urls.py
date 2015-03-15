__author__ = 'Taylor'
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

import views


urlpatterns = patterns('',
    # Gets a random question
    url(r'^$', views.get_random_question),
    # Gets a specific question
    url(r'^(?P<pk>\d+)/$', views.QuestionDetail.as_view()),
    #  Create a Question
    url(r'^create$', views.create_question),
    # Provide answer to question
    url(r'^(?P<pk>\d+)/positive$', views.answer_positive),
    url(r'^(?P<pk>\d+)/negative$', views.answer_negative),
)

urlpatterns = format_suffix_patterns(urlpatterns)