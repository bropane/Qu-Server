from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qu_x.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
