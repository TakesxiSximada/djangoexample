# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ping(request):
    return HttpResponse('PONG')