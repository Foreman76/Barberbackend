# -*- coding: utf-8 -*-


from rest_framework import serializers
from .models import BarberNews


class userinfo(object):

    def __init__(self, token, phone, nUser):
        self.token = token
        self.phone = phone
        self.nUser = nUser

class serializeruserinfo(serializers.Serializer):
                        
    token = serializers.CharField()        
    phone = serializers.CharField()
    nUser = serializers.CharField()

class serializerlistnews(serializers.ModelSerializer):
    class Meta:
        model = BarberNews
        fields = ['bTitleNews', 'bTextNews', 'bNewsDate']
        

