# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .models import Users
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "users/usersIndex.html")
def register(request):
    if request.method == 'POST':
        valid = Users.userManager.register(
            request.POST['name'],
            request.POST['last'],
            request.POST['email'],
            request.POST['password'],
            request.POST['confirmation']
        )
        if valid[0]:
		    request.session["email"] = {
		    "id": valid[1].id,
		    "name": valid[1].name
		    }
                    return redirect("users/users")
        else:
            for errors in valid[1]:
                messages.add_message(request, messages.ERROR, errors)
            return redirect("/register")
    elif request.method == 'GET':
        return render(request, "users/register.html")
def new_session(request):
    if request.method == 'POST':
        valid = Users.userManager.login(
            request.POST["email"],
            request.POST["password"],
        )
        if valid[0]:
            request.session["email"] = {
		        "id": valid[1].id,
		        "name": valid[1].name
		    }
            return redirect("/users")
        else:
            for errors in valid[1]:
                messages.add_message(request, messages.ERROR, errors)
        return redirect("/login")
    if request.method == 'GET':
        return render(request, "users/usersLogin.html")

    # email = request.POST.get['email']
    # password = request.POST.get['password']
    # user = authenticate(email=email, password=password)
    # if user is not False:
    #     if user is True:
    #         # login(request, user)
    #         return redirect("/users")
    #     else:
    #         return redirect("/login")
    # else:
    #     return redirect("/login")
def users(request):
    return render(request, "users/usersList.html")
