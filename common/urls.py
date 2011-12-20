from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dotpy',
    url(r'^$', 'common.views.user', name='user'),
    url(r'^n/$', 'notes.views.notes', name='user-notes'),
    url(r'^p/$', 'projects.views.projects', name='user-projects'),
)
