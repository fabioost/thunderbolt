from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			messages.info(request, "Usuário Cadastrado com Sucesso!")
			#success_url = reverse_lazy('login')
			return redirect("/users/user_cad_sucess")
		else: 
			for msg in form.error_messages:
				print(form.error_messages[msg])
			return render(request = request,
						  template_name = "users/register.html",
						  context={"form":form})


	form = CustomUserCreationForm()
	return render(request=request,
				  template_name= "users/register.html",
				  context={"form":form})


@login_required
def user_cad_sucesso(request):
	return render(request=request,
				  template_name="users/user_cad_sucess.html",
				  context={})