# -*- coding: utf-8 -*-


from rest_framework import serializers
from .models import *


class UserInfo(object):

    def __init__(self, token, phone, nUser):
        self.token = token
        self.phone = phone
        self.nUser = nUser

class SerializerUserInfo(serializers.Serializer):
                        
    token = serializers.CharField()        
    phone = serializers.CharField()
    nUser = serializers.CharField()

class SerializerListNews(serializers.ModelSerializer):
    class Meta:
        model = BarberNews
        fields = ['bTitleNews', 'bTextNews', 'bNewsDate']
        
class SerializerListServices(serializers.ModelSerializer):
    class Meta:
        model = BarberService
        fields = ['id', 'bService', 'bPrice']        

class SerializerListMasters(serializers.ModelSerializer):
    class Meta:
        model = BarberMasters
        fields = ['id', 'bMaster']

class SerializerListServiceTime(serializers.ModelSerializer):
    class Meta:
        model = ServiceTime
        fields = ['id', 'bTime']        