from django.contrib import admin
from django.urls import path, include

from .views import HomePageView
from . import views

from django.conf import settings
from django.conf.urls.static import static
#app_name= "main" #nao funciona

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("entrada/", views.nova_entrada, name="nova_entrada"),
    path("cad_home/", views.cad_home, name="cad_home"),
    #path("photo_page/", views.photo_page, name="Foto"),
    #path("upload_photo/", views.upload_photo, name="Foto"),
    #caddecampo
    #path('', include('caddecampo.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
