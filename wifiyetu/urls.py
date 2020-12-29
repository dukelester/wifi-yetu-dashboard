from django.urls import path
from .views import aboutPage_view, helpPage_view, contactusPage_view, privacyPage_view, passwordResetPage_view, \
    termsPage_view, captiveloginPage_view, registerPage_view,portalLoginPage_view,homePage_view,profileview,marketting,editpackage,deletepackage,charts

urlpatterns = [
    path('', homePage_view, name='home'),
    path('about/', aboutPage_view, name='about'),
    path('help/', helpPage_view, name='help'),
    path('contact/', contactusPage_view, name='contact'),
    path('privacy/', privacyPage_view, name='privacy'),
    path('reset/', passwordResetPage_view, name='reset'),
    path('terms/', termsPage_view, name='terms'),
    path('captivelogin/', captiveloginPage_view, name='captivelogin'),
    path('portalregister/', registerPage_view, name='portalregister'),
    path('portallogin/', portalLoginPage_view, name='portalLogin'),
    path('profile',profileview,name='profile'),
    path('charts',charts,name='charts'),
    path('deletepackage',deletepackage,name='deletepackages'),
    path('editpackage',editpackage,name='editpackages'),
    path('marketting',marketting,name='marketting'),
    ]
