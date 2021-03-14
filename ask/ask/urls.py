from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'test', name='home'),
    url(r'^login/', 'test'),
    url(r'^signup', 'test'),
    url(r'^question/(?P<id>\d+)', 'test', name='question'),
    url(r'^ask/', 'test', name='ask'),
    url(r'^popular/', 'test', name='popular'),
    url(r'^new', 'test'),
    url(r'^answer/$', 'test', name='answer'),
)
