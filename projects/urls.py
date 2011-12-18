from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dotpy.projects.views',
    url(r'^$', 'projects', name='projects'),
    url(r'^(\d+)/$', 'project', name='project'),
)
