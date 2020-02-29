# -*- coding: utf-8 -*-


from rest_framework import serializers


class userinfo(object):

    def __init__(self, token, phone, nUser):
        self.token = token
        self.phone = phone
        self.nUser = nUser

class serializeruserinfo(serializers.Serializer):
                        
    token = serializers.CharField()        
    phone = serializers.CharField()
    nUser = serializers.CharField()