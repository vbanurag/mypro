"""web1 URL Configuration

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
    
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,"show_indexes":False}),
    
    url(r'^aboutus$', 'web1.views.aboutus', name='aboutus'),
    url(r'^blog$', 'web1.views.blog', name='blog'),
    url(r'^foer$', 'web1.views.foer', name='foer'),
    url(r'^forms$', 'web1.views.forms', name='forms'),
    url(r'^formsubmit/$', 'web1.views.formsubmit', name='formsubmit'),
    url(r'^form1$', 'web1.views.form1', name='form1'),
    url(r'^formsubmit1/$', 'web1.views.formsubmit1', name='formsubmit1'),
    
    url(r'^value/(?P<myval>\d+)$','web1.views.display',name='display'),
    url(r'^project_mca$', 'web1.views.project_mca', name='project_mca'),
    

    url(r'^$', 'web1.views.home', name='home'),


    url(r'^signup$', 'web1.views.user_signup', name='user_signup'),
    url(r'^login_project$', 'web1.views.login_project', name='login_project'),
    url(r'^user_page$', 'web1.views.user_page', name='user_page'),
    
    url(r'^project$', 'web1.views.project', name='project'),
    
    url(r'^project_res$', 'web1.views.project_res', name='project_res'),
    url(r'^project_mtech$', 'web1.views.project_mtech', name='project_mtech'),
    url(r'^project_mca$', 'web1.views.project_mca', name='project_mca'),
    #url(r'^helpinghand$', 'web1.views.helpinghand', name='helpinghand'),

    url(r'^project_desc/(?P<myvalue>/d+)$', 'web1.views.project_desc', name='project_desc'),

    #for dynamically displaying the projects

    #url(r'^detail/(?P<t_id>\d+)$', 'web1.views.project_dislpay', name='project_display'),
    

    url(r'^helpinghand$', 'web1.views.helpinghand_form', name='helpinghand_form'),
    url(r'^battijalao$', 'web1.views.battijalao_form', name='battijalao_form'),

    
    
    # url(r'^search/$', include('haystack.urls')),

]

