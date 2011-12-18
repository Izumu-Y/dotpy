from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dotpy.notes.views',
    url(r'^$', 'notes', name='notes'),
    url(r'^(\d+)/$', 'note', name='note'),
)
