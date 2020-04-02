from django.urls import path
from .views import SignUpView, register, user_cad_sucesso
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("register/", views.register, name="register"),
    path("user_cad_sucess/", views.user_cad_sucesso, name="user_cad_sucesso"),
]