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
    
    
    
    url(r'^foer$', 'web1.views.foer', name='foer'),
   
    
    
    
    

    url(r'^$', 'web1.views.home', name='home'),


    url(r'^signup$', 'web1.views.user_signup', name='user_signup'),
    url(r'^login_project$', 'web1.views.login_project', name='login_project'),
    url(r'^user_page$', 'web1.views.user_page', name='user_page'),


    
    url(r'^project$', 'web1.views.project', name='project'),
    url(r'^project_res$', 'web1.views.project_res', name='project_res'),
    url(r'^project_mtech$', 'web1.views.project_mtech', name='project_mtech'),
    url(r'^project_mca$', 'web1.views.project_mca', name='project_mca'),
    url(r'^project_detail$', 'web1.views.project_detail', name='project_detail'),
    url(r'^project_bsc$', 'web1.views.project_bsc', name='project_bsc'),
    url(r'^project_btech$', 'web1.views.project_btech', name='project_btech'),

    url(r'^detail/(?P<myvalue>\d+)/$', 'web1.views.project_desc', name='project_desc'),
    url(r'^detailug/(?P<myvalue>\d+)/$', 'web1.views.project_desc_undergrad', name='project_desc_undergrad'),
    url(r'^detailri/(?P<myvalue>\d+)/$', 'web1.views.project_desc_ri', name='project_desc_ri'),
    #for dynamically displaying the projects

    #url(r'^detail/(?P<t_id>\d+)$', 'web1.views.project_dislpay', name='project_display'),
    

    url(r'^helpinghand$', 'web1.views.helpinghand_form', name='helpinghand_form'),
    url(r'^battijalao$', 'web1.views.battijalao_form', name='battijalao_form'),

    url(r'^contact_us$', 'web1.views.contact_us', name='contact-us'),
    
    # url(r'^search/$', include('haystack.urls')),

]

