# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include
from wifiyetu.views import  admindashboard# add this

# from mpesa.urls import mpesa_urls

urlpatterns = [
    # path('admin/', admin.site.urls),          # Django admin route
    path('admin/', admin.site.urls),  # Django admin route
    path("auth", include("authentication.urls")),  # Auth routes - login / register
    path("dashboard/", include("app.urls")),  # UI Kits Html files
    path("api/payments/", include("mpesa.api.urls")),
    path('auth/', include('django.contrib.auth.urls')),
    path("", include('wifiyetu.urls')),
    path("mpesa2", include('mpesa_api.urls')),
    path('social-auth', include('social_django.urls', namespace='social')),



]
