# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


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
