# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models.functions import Coalesce
from rest_framework.views import APIView
from django.views.generic import ListView
import requests
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializer import RouterSerializer
from .models import Router


# Create your views here.

class RouterList(generics.ListCreateAPIView):

	serializer_class = RouterSerializer

	def get_queryset(self):
		
		result = None
		sid = self.request.GET.get('sid')
		ipstart = self.request.GET.get('ipstart') 
		ipend = self.request.GET.get('ipend')

		if sid:
			
			result = Router.objects.filter(sapid = sid)
		
		elif ipstart and ipend:
		
			if ipstart < ipend:
				min_ip = ipstart
				max_ip = ipend
			else:
				min_ip = ipend
				max_ip = ipstart

			result = Router.objects.filter(loopback__range = (min_ip,max_ip))
		
		else:
		
			result = Router.objects.all()
		
		return result

	def create(self, request, *args, **kwargs):
		"""Save the post data """
		
		data = self.request.POST
		sapid = data.get('sapid',None)
		hostname = data.get('hostname',None)
		loopback = data.get('loopback',None)
		mac = data.get('loopback',None)
		router = Router(sapid = sapid, hostname = hostname, loopback = loopback, mac = mac)
		router.save()
		serializer = RouterSerializer(router)
		return Response(serializer.data)
    	

class RouterDetail(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = RouterSerializer
	queryset = Router.objects.all()
	lookup_field = 'loopback'
