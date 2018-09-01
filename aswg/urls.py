"""skyguard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# -*- coding:utf-8 -*-
from django.conf.urls import include, url #patterns
from django.contrib import admin
from django.urls import path
from . import views

"""
urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'aswg/login', views.login),
    url(r'aswg/index', views.index),
    url(r'get_classes.html$', views.get_classes),
    url(r'add_classes.html$', views.add_classes),
    url(r'del_classes.html$', views.del_classes),
    url(r'edit_classes.html$', views.edit_classes),
    url(r'base$', views.base),
    url(r'load$', views.loading),
    url(r'logout', views.logout),
    url(r'jstest',views.jstest),
    url(r'^search_form$', views.search_form),
    url(r'^search$', views.search),
    url(r'^search-post$', views.search_post),
    url(r'upload$', views.upload_file),
    url(r'^ajax_get$',views.ajax_get),
    url(r'^ajax_post$',views.ajax_post),
    url(r'jsonp$',views.ajax_jsonp),
    url(r'post$',views.params_post),
    
]
