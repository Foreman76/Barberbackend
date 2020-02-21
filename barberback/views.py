# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import BarberProfile
from django.contrib.auth.models import User
from barberback.serializers import userinfo, serializeruserinfo

# Create your views here.

def testv(request):
    b = userinfo('2345789876543234567', '01293841987587')
    ser = serializeruserinfo(b)
    print(ser.data)
    return JsonResponse(data=ser.data)