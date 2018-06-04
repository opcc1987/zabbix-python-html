# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from  models import Groups
from django.template import loader, Context
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html')

def report(request):
    posts = Groups.objects.all()
    t = loader.get_template("show.html")
#    c = Context({ 'posts' : posts })
    c = t.render({'posts':posts})
    return HttpResponse(c)

def old_report(request):
    return HttpResponseRedirect(
        reverse('report')
    )


