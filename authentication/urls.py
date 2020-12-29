# -*- encoding: utf-8 -*-
from django.conf.urls import url
from django.urls import path, include
from .views import login_view, user_registration,google_login,admin_login_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('authlogin/', login_view, name="authlogin"),
    path('registeruser/', user_registration, name="registeruser"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("google", google_login, name="google_login"),
    path('admin_login_view',admin_login_view,name='admin_login_view')
    # url('^', include('django.contrib.auth.urls')),

    # password reset.
    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
