from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from app import settings
from home import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    url(r'^home$', views.home, name='home'),
    url(r'^availability', views.availability, name='pravailabilityofile'),
    url(r'^rides', views.rides, name='rides'),
    url(r'^request', views.request, name='request'),
    url(r'^logout$', views.logout, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
)

urlpatterns += patterns('',
 (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
 )
