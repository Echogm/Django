# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    return render(request, "users/usersIndex.html")
def register(request):
    return render(request, "users/usersRegister.html")
def login(request):
    return render(request, "users/usersLogin.html")
def users(request):
    return render(request, "users/usersList.html")
