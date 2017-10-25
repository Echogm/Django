# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .models import Users, Trip, Travelers
from django.contrib import messages
from django.contrib.auth import authenticate, login
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
            return redirect("/travels")
        else:
            for errors in valid[1]:
                messages.add_message(request, messages.ERROR, errors)
        return redirect("/login")
    if request.method == 'GET':
        return render(request, "users/usersLogin.html")

def logout(request):
    request.session.clear()
    return redirect("/register")

def travels(request):
    if 'email' not in request.session:
        return redirect('/login')
    if request.method == 'GET':
		context = {
			"travelers": Trip.objects.all(),
			"email": Travelers.travelersManager.filter(traveler_id=request.session["email"]["id"])
		}
		return render(request, "users/travels.html", context)
    elif request.method == 'POST':
		Trip.objects.create(
			destination=request.POST["destination"],
			description=request.POST["description"],
			travel_start_date=request.POST["travel_start_date"],
			travel_end_date=request.POST["travel_end_date"],
			creator_id=request.session["email"]["id"]
		)
		return redirect('/travels')
    # return render(request, "users/travelers.html")

def addplan(request):
    if 'email' not in request.session:
		return redirect('/')
    return render(request, "users/addplan.html")

def users(request):
    return render(request, "users/usersList.html")
