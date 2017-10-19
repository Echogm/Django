# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime
from time import gmtime, strftime
# Create your views here.
# Indexpage.
def index(request):
    now = {
        "time": strftime("%b %a, %Y %r", gmtime())
    }
    return render(request, 'time_display/timeDisplayIndex.html',now)
