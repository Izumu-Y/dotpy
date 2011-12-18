from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dotpy.common.views.home', name='home'),
    url(r'^users/$', 'dotpy.common.views.users', name='users'),
    url(r'^users/([\w.-]{1,30})/$', 'dotpy.common.views.user', name='user'),

    url(r'^notes/', include('dotpy.notes.urls')),

    # url(r'^dotpy/', include('dotpy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
