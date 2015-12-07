# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


"""
Giriş sayfası
"""


@csrf_exempt
def index(request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if username and password and user and user.is_active:
            login(request, user)
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


@login_required()
@csrf_exempt
def logout_view(request):
    logout(request)
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
