from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from questions import views

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qu_x.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
