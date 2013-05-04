from django.conf.urls import patterns, include, url
from app.views import home, done, logout, error, form, form2, close_login_popup

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^$', home, name='home'),
    url(r'^done/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^form/$', form, name='form'),
    url(r'^form2/$', form2, name='form2'),
    url(r'^close_login_popup/$', close_login_popup, name='login_popup_close'),

    url(r'', include('social_auth.urls')),
    # Examples:
    # url(r'^$', 'Tumblr.views.home', name='home'),
    # url(r'^Tumblr/', include('Tumblr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
