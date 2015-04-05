from django.conf.urls import patterns, include, url
from sistema import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'si_webservice.views.home', name='home'),
    # url(r'^si_webservice/', include('si_webservice.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cadastrar/$', views.cadastrar, name='home'),
    url(r'^teste/$', views.teste, name='teste'),

    url(r'^auth/', include('djoser.urls')),


)
