"""megapolia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path, path
from megagames import views


urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^(?P<pid>\d{4})/', views.player),
    re_path(r'^login', views.loginU),
    re_path(r'^logout', views.logoutU),
    re_path(r'^(?P<pid>\d{4})/', views.player),
    re_path(r'^stat3', views.stat3),
    re_path(r'^stat10', views.stat10),
    #re_path(r'^testfill', views.fill_db),
    path('admin/', admin.site.urls),
    path('all_players/', views.all_players),


    url(r'^addWin/(?P<pid>\d+)/(?P<code>\D+)', views.addWinScore, name="win-score-url"),
    url(r'^addPlay/(?P<pid>\d+)/(?P<code>\D+)', views.addPlayScore, name="play-score-url"),
]
