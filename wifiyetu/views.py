# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from  authentication.models import UserProfile


def homePage_view(request):
    return render(request, 'home.html')


def aboutPage_view(request):
    return render(request, 'about.html')


def helpPage_view(request):
    return render(request, 'help.html')


def privacyPage_view(request):
    return render(request, 'privacy.html')


def contactusPage_view(request):
    return render(request, 'contactus.html')


def passwordResetPage_view(request):
    return render(request, 'passwordReset.html')


def termsPage_view(request):
    return render(request, 'terms.html')


def registerPage_view(request):
    return render(request, 'register.html')


def captiveloginPage_view(request):
    return render(request, 'login.html')


def portalLoginPage_view(request):
    return render(request, 'portalLogin.html')


@login_required()
def profileview(request):


    return render(request,'profile.html')

def marketting(request):
    return render(request, 'marketting.html')


def editpackage(request):
    return render(request, 'editpackage.html')


def  deletepackage(request):
    return render(request, 'deletepackage.html')


def charts(request):
    return render(request, 'charts.html')

@login_required()
def admindashboard(request):
    if request.user.is_superuser:
        return render(request, '')
    else:
        return HttpResponse('This page is only accessible to admins')



