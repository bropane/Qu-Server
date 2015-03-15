__author__ = 'Taylor'
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from questions import views

router = DefaultRouter()
router.register(r'', views.QuestionViewSet)

urlpatterns = patterns('',
    # Gets a random question
    url(r'^', include(router.urls)),
    # Provide answer to question
    # url(r'^(?P<pk>\d+)/positive$', views.),
    # url(r'^(?P<pk>\d+)/negative$', views.),
)