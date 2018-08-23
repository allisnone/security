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
from django.conf.urls import include, url#,patterns
from django.contrib import admin
from django.urls import path
#import aswg.views

urlpatterns = [
    #path('admin/', admin.site.),
    url(r'', include('aswg.urls')),
]


"""

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app1/login/', views.login),
    url(r'^app1/index/', views.index),
    url(r'^get_classes.html', views.get_classes),
    url(r'^add_classes.html', views.add_classes),
    url(r'^del_classes.html', views.del_classes),
    url(r'^edit_classes.html', views.edit_classes),
]
"""

"""

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('user.urls')),
    url(r'^', include('dashboard.urls')),
    url(r'^', include('report.urls')),
    url(r'^', include('config.urls')),
    url(r'^', include('about.urls')),
    url(r'^', include('load.urls')),
#    url(r'^', include('old_dashboard.urls')),
)
"""