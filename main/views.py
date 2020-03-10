from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EntradaTeste

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


def nova_entrada(request):
	if request.method == "POST":
		form = EntradaTeste(request.POST)
		if form.is_valid():
			messages.info(request, "Entrada Registrada com Sucesso!")
			return redirect("/")
		else: 
			for msg in form.error_messages:
				print(form.error_messages[msg])
			return render(request = request,
						  template_name = "main/entrada.html",
						  context={"form":form})

	form = EntradaTeste()
	return render(request=request,
				  template_name= "main/entrada.html",
				  context={"form":form})