# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    if not 'count'in request.session:
        request.session['count'] = 0
        return render(request, "random_word/random_wordIndex.html")
    else:

        return render(request, "random_word/random_wordIndex.html")

def random(request):
    request.session['count'] += 1
    request.session['randomword'] = get_random_string(length=32)
    return redirect("/random_word")

def reset(request):
    request.session.clear()
    return redirect('/random_word')
