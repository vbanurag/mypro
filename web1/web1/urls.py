"""new1 URL Configuration

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


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^photo/$', 'pic.views.photo'),
    url(r'^media/(.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,'show_indexes':False}),
    url(r'^$', 'new1.views.home', name='home'),
    url(r'^aboutus$', 'new1.views.aboutus', name='aboutus'),
    url(r'^blog$', 'new1.views.blog', name='blog'),
    url(r'^foer$', 'new1.views.foer', name='foer'),
    url(r'^forms$', 'new1.views.forms', name='forms'),
    url(r'^formsubmit/$', 'new1.views.formsubmit', name='formsubmit'),
    url(r'^form1$', 'new1.views.form1', name='form1'),
    url(r'^formsubmit1/$', 'new1.views.formsubmit1', name='formsubmit1'),
    url(r'^login1$', 'new1.views.login1', name='login1'),
    url(r'^logout1$', 'new1.views.logout1', name='logout1'),
    url(r'^signup$', 'new1.views.login_submit', name='login_submit'),
    url(r'^login_cumplete/$', 'new1.views.signup', name='signup'),
    url(r'^value/(?P<myval>\d+)$','new1.views.display',name='display'),
    url(r'^project_mca$', 'new1.views.project_mca', name='project_mca'),
   # url(r'^contact-us$', 'new1.views.contact-us', name='contact-us'),
   # url(r'^search/$', include('haystack.urls')),
]
