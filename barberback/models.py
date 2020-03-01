# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BarberProfile(models.Model):
    
    class Meta:
        db_table = 'barber_profile'

    Barber_Phone = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='Телефон пользователя')
    Barber_User  = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    
    def __unicode__(self):
        return '%s %s' % (self.Barber_User, self.Barber_Phone)


class BarberService(models.Model):

    class Meta:
        db_table = 'barber_service'

    bService = models.CharField(max_length=200, verbose_name='Наименование услуги') 
    bPrice   = models.DecimalField(verbose_name='Цена услуги', max_digits=15, decimal_places=2) 

    def __unicode__(self):
        return '%s %s' % (self.bService, self.bPrice) 

class BarberNews(models.Model):

    class Meta:
        db_table = 'barber_news'
        ordering = ['bNewsDate']

    bTitleNews = models.CharField(max_length=150, verbose_name='Заголовок')
    bTextNews  = models.TextField(verbose_name='Текст новости')
    bNewsDate  = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def save(self, *args, **kwargs):
        super(BarberNews, self).save(*args, **kwargs)

        ListUser = User.objects.filter(is_superuser=False)
        for lUser in ListUser:
            lFields = {'bNewsUser':lUser, 'bNews':self, 'bSend':False}
            BarberUserSendNews.objects.update_or_create(bNewsUser=lUser, bNews=self , defaults=lFields)


    def __unicode__(self):
        return '%s %s' % (self.bNewsDate, self.bTitleNews)

class BarberUserSendNews(models.Model):

    class Meta:
        db_table = 'barber_sendNews'

    bNewsUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bNewsUser')
    bNews     = models.ForeignKey(BarberNews, on_delete=models.CASCADE, related_name='bNews')       
    bSend     = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s %s' % (self.bNewsUser, self.bNews.bTitleNews, self.bSend)






