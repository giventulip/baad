from django.urls import path

#############################
from navigationbar.views import navbar

urlpatterns = [
    path('',navbar, name="navbar")
]