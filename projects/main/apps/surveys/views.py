# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# Create your views here.
# NOTE: Missing page
def index(request):
    return render(request, "surveys/surveysIndex.html")

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    if request.session['name'] < 3:
        print "less than 3"
        return redirect("/surveys")
    elif request.session['location'] == "null":
        print "Error 444"
        return redirect("/surveys")

    return redirect("/surveys")
def result(request):
    return render(request, "surveys/surveydisplay.html")
