# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BarberProfile(models.Model):
    
    class Meta:
        db_table = 'barber_profile'

    Barber_Phone = models.CharField(max_length=20, unique=True, db_index=True)
    Barber_User  = models.OneToOneField(User, on_delete=models.CASCADE)
    




