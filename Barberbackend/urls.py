"""Barberbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from barberback.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/getuserinfo/', GetUserInfo.as_view()),
    url(r'^api/v1/register/', CreateBarber.as_view()),
    url(r'^api/v1/getlistnewsuser', GetListNewsUser.as_view()),
    url(r'^api/v1/getlistservices', GetListServices.as_view()),
    url(r'^api/v1/getlistmasters', GetListMasters.as_view()),
    url(r'^api/v1/getlisttime/', GetListServicesTime.as_view())
]
