# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class Router(models.Model):
	""" Router model """

	sapid = models.CharField(max_length = 18)
	hostname = models.CharField(max_length = 14)
	loopback = models.GenericIPAddressField()
	mac = models.CharField(max_length = 17)

	def __str__(self):
		return ' '.join(self.sapid,self.hostname,self.loopback,self.mac)

	class Meta:
		unique_together = ('hostname' , 'loopback')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



