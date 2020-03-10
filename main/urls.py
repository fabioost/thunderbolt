from django.contrib import admin
from django.urls import path, include

from .views import HomePageView
from . import views

#app_name= "main" #nao funciona

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("entrada/", views.nova_entrada, name="nova_entrada"),
]