# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template


@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def baseView(request):
    return render(request, 'base.html')


# @login_required(login_url="/login/")
def baseFullScreenView(request):
    return render(request, 'base-fullscreen.html')


@login_required(login_url="/login/")
def indexView(request):
    return render(request, 'index.html')


@login_required(login_url="/login/")
def dashboardView(request):

    return render(request, 'dashboard.html')


@login_required(login_url="/login/")
def bootsrapTablesView(request):
    return render(request, 'bootstrap-tables.html')


@login_required(login_url="/login/")
def lockView(request):
    return render(request, 'lock.html')


@login_required(login_url="/login/")
def page403View(request):
    return render(request, 'page-403.html')


@login_required(login_url="/login/")
def page404View(request):
    return render(request, 'page-404.html')


@login_required(login_url="/login/")
def page500View(request):
    return render(request, 'page-500.html')


@login_required(login_url="/login/")
def settingsView(request):
    return render(request, 'settings.html')


@login_required(login_url="/login/")
def transactionsView(request):
    return render(request, 'transactions.html')



@login_required(login_url="/login/")
def uiButtonsView(request):
    return render(request, 'ui-buttons.html')

@login_required(login_url="/login/")
def uiFormsView(request):
    return render(request, 'ui-forms.html')

@login_required(login_url="/login/")
def uiModalsView(request):
    return render(request, 'ui-modals.html')

@login_required(login_url="/login/")
def uiNotificationsView(request):
    return render(request, 'ui-notifications.html')



def signUpView(request):
    return render(request, 'sign-up.html')


# @login_required(login_url="/login/")
def signInView(request):
    return render(request, 'sign-in.html')


# @login_required(login_url="/login/")
def forgotPasswordView(request):
    return render(request, 'forgot-password.html')


# @login_required(login_url="/login/")
def resetPasswordView(request):
    return render(request, 'reset-password.html')

def registerView(request):
    return render(request, 'register.html')



def loginView(request):
    return render(request, 'login.html')


