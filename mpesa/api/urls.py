from django.urls import include, path
from .views import LNMCallbackUrlAPIView
urlpatterns = [
    path('lnm/', LNMCallbackUrlAPIView.as_view(), name="lnm-callback-url"),
]