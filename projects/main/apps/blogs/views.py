# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
# Indexpage.
def index(request):
    response = "Blog"
    return HttpResponse(response)

def new(request):
    response = "New form for a blogs post."
    return HttpResponse(response)

def create(request):
    response = "Create a new post here."
    return HttpResponse(response)

def show(request, number):
    response = "Place Holder id {}".format(number)
    return HttpResponse(response)

def edit(request,number):
    response = "Edit Post {}".format(number)
    return HttpResponse(response)

def delete(request,number):
    response = "Delete Post {}".format(number)
    return HttpResponse(response)
