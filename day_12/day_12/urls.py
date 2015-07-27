"""day_12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^photo/$', 'pic.views.photo'),
    url(r'^media/(.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,'show_indexes':False}),
    #url(r'^$', 'day_12.views.home', name='home'),
    url(r'^aboutus$', 'day_12.views.aboutus', name='aboutus'),
    url(r'^blog$', 'day_12.views.blog', name='blog'),
    url(r'^foer$', 'day_12.views.foer', name='foer'),
    url(r'^forms$', 'day_12.views.forms', name='forms'),
    url(r'^formsubmit/$', 'day_12.views.formsubmit', name='formsubmit'),
    url(r'^form1$', 'day_12.views.form1', name='form1'),
    url(r'^formsubmit1/$', 'day_12.views.formsubmit1', name='formsubmit1'),
    url(r'^login1$', 'day_12.views.login1', name='login1'),
    url(r'^logout1$', 'day_12.views.logout1', name='logout1'),
    url(r'^signup$', 'day_12.views.login_submit', name='login_submit'),
    url(r'^login_cumplete/$', 'day_12.views.signup', name='signup'),
    url(r'^value/(?P<myval>\d+)$','day_12.views.display',name='display'),
    url(r'^search/$', include('haystack.urls')),
    #url(r'^loginp$', 'day_12.views.login_project', name='login_project'),
    url(r'^logouts$', 'day_12.views.logout_project', name='logout_project'),
    url(r'', include('social_auth.urls')),
    url(r'^loginp/$', RedirectView, {'url': '/loginp/github'}),
    url(r'^private/$', 'day_12.views.private'),
]
