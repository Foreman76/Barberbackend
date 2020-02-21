# -*- coding: utf-8 -*-


from rest_framework import serializers


class userinfo(object):

    def __init__(self, token, phone):
        self.token = token
        self.phone = phone

class serializeruserinfo(serializers.Serializer):
                        
    token = serializers.CharField()        
    phone = serializers.CharField()