# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from .models import BarberProfile, BarberUserSendNews, BarberNews
from django.contrib.auth.models import User
from barberback.serializers import userinfo, serializeruserinfo, serializerlistnews
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token

class GetUserInfo(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]

    def get(self, request, formant=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):

        lToken = Token.objects.get(user=request.user)

        lUserInfo = userinfo(lToken, request.user.username, request.user.last_name)
        content = serializeruserinfo(lUserInfo)
        return Response(content.data)



class GetListNewsUser(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):

        #Определим есть ли новости для пользователя
        lUser = request.user
        lListPk = []
        lNewsForSend = BarberUserSendNews.objects.filter(bNewsUser=lUser, bSend=False)
        for newssend in lNewsForSend:
            lListPk.append(newssend.bNews.pk)
        lNewsForSend.update(bSend=True)

        lNews = BarberNews.objects.filter(pk__in=lListPk)
        content = serializerlistnews(lNews, many=True)
        return Response(content.data)



class CreateBarber(APIView):

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

        
    