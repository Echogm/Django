# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    response = "Index"
    return HttpResponse(response)
def new(request):
    response = "New form for a blogs post."
    return HttpResponse(response)
def create(request):
    response = "Create a new post here."
