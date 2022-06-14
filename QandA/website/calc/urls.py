"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("",views.index),
    path("login",views.login),
    path("index_login",views.index_login),
    path("home_feed",views.home_feed),
    path("signup",views.signup),
    path("feed",views.feed),
    path("comment",views.comment),
    path("profile",views.profile),
    path("notification",views.notification),
    path("settings",views.settings),
    path("add",views.add),
    path("search",views.search_q),
]
