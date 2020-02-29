# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from .models import BarberProfile
from django.contrib.auth.models import User
from barberback.serializers import userinfo, serializeruserinfo
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token

class testv(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        lToken = Token.objects.get(user=request.user)

        b = userinfo(lToken, request.user.username, request.user.last_name)
        content = serializeruserinfo(b)
        return Response(content.data)



# Create your views here.



class create_barberprofile(APIView):

    lNotExist = False

    def get(self, request, format=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def post(self, request, format=None):
        
        try:
            lUser = User.objects.get(username=request.data['phone'])
            lToken = Token.objects.get(user=lUser)
            b = userinfo(token=lToken, phone=lUser.username, nUser=lUser.last_name)
            content = serializeruserinfo(b)
            return Response(content.data)
        except User.DoesNotExist:
            self.lNotExist = True

        if self.lNotExist:
            #Создадим пользователя 
            lUser = User.objects.create_user(request.data['phone'], 'lennon@thebeatles.com', request.data['phone']+'Qwsaq')
            lUser.last_name = ''
            lUser.save()

            lToken = Token.objects.create(user=lUser)
            #Здесь можно создать профиль если понадобиться
            #BarberProfile.objects.create(Barber_Phone=lUser.username, Barber_User=lUser)
            b = userinfo(token=lToken, phone=lUser.username, nUser=lUser.last_name)
            content = serializeruserinfo(b)
            return Response(content.data)

        
    