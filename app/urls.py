# -*- encoding: utf-8 -*-
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from app import views
from app.views import indexView, dashboardView, forgotPasswordView, uiFormsView, uiModalsView, \
    uiNotificationsView, uiButtonsView, settingsView, registerView, resetPasswordView, signInView, signUpView, \
    lockView, loginView, transactionsView, page403View, page404View, page500View, bootsrapTablesView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*/dashboard/.*', views.pages, name='pages'),

    path('index', indexView, name='index'),
    path('base', views.baseView, name='base'),
    path('basefullscreen', views.baseFullScreenView, name='basefullscreen'),
    path('dashboard', dashboardView, name='dashboard'),
    path('transactions', transactionsView, name='transactions'),
    path('page403', page403View, name='page403'),
    path('page404', page404View, name='page404'),
    path('page500', page500View, name='page500'),
    path('bootsrapTables', bootsrapTablesView, name='bootsrapTables'),
    path('signUp', signUpView, name='signUp'),
    path('login', loginView, name='login'),
    path('signIn', signInView, name='signIn'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('lock', lockView, name='lock'),
    path('register', registerView, name='register'),
    path('settings', settingsView, name='settings'),
    path('resetPassword', resetPasswordView, name='resetPassword'),
    path('forgotPassword', forgotPasswordView, name='forgotPassword'),
    path('uiNotifications', uiNotificationsView, name='uiNotifications'),
    path('uiButtons', uiButtonsView, name='uiButtons'),
    path('uiForms', uiFormsView, name='uiForms'),
    path('uiModals', uiModalsView, name='uiModals'),

]
