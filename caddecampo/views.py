from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Propriedade, Area, Defensivo, Adubo, Colheita, AplicacaoDefensivo, AplicacaoAdubo #Apontamento, Apontamento_teste
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserChangeForm, CustomUserCreationForm, CadastroAduboForm, CadastroAreaForm, CadastroPropriedadeForm, CadastroDefensivoForm,  CadastroColheitaForm,  CadastroAplicacaoDefensivoForm, CadastroAplicacaoAduboForm

from django.views.generic import View

from .utils import render_to_pdf
from datetime import datetime

def homepage(request):
	#return HttpResponse("Woe this is an <strong> awesome</strong> tuotorial")
	if request.user.is_authenticated:
		defensivos = AplicacaoDefensivo.objects.filter(area__propriedade__owner=request.user, apontamento_published=datetime.now())
		adubos = AplicacaoAdubo.objects.filter(area__propriedade__owner=request.user, apontamento_published=datetime.now())
		colheitas = Colheita.objects.filter(area__propriedade__owner=request.user, apontamento_published=datetime.now())
		return render(request=request,
				  template_name="caddecampo/home.html",
				  context={"defensivos": defensivos,
						   "adubos":adubos,
						   "colheitas":colheitas
						  })#

	return render(request=request,
				  template_name="caddecampo/home.html",
				  context={})#


def desenvolvedor(request):
	#return HttpResponse("Woe this is an <strong> awesome</strong> tuotorial")

	return render(request=request,
				  template_name="caddecampo/desenvolvedor.html",
				  context={})#


@login_required
def novo_apontamento(request, id=0):
	return render(request=request,
				  template_name="caddecampo/novo_apontamento.html",
				  context={"id":id})#



@login_required
def novo_cadastro(request):
	return render(request=request,
				  template_name="caddecampo/novo_cadastro.html",
				  context={})#



@login_required
def apt_sucesso(request):
	return render(request=request,
				  template_name="caddecampo/apt_sucess.html",
				  context={})#

@login_required
def editar_sucesso(request):
	return render(request=request,
				  template_name="caddecampo/editar_sucess.html",
				  context={})#



@login_required
def cad_sucesso(request):
	return render(request=request,
				  template_name="caddecampo/cad_sucess.html",
				  context={})#

@login_required
def deletar_sucess(request):
	return render(request=request,
				  template_name="caddecampo/deletar_sucess.html",
				  context={})

@login_required
def cad_editar_sucesso(request):
	return render(request=request,
				  template_name="caddecampo/cad_editar_sucess.html",
				  context={})


@login_required
def user_cad_sucesso(request):
	return render(request=request,
				  template_name="caddecampo/user_cad_sucess.html",
				  context={})#{"tutorials": Tutorials.objects.all})


def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			login(request, user)
			messages.info(request, "Usuário Cadastrado com Sucesso!")
			return redirect("/user_cad_sucess")
		else: 
			for msg in form.error_messages:
				print(form.error_messages[msg])
			return render(request = request,
						  template_name = "caddecampo/register.html",
						  context={"form":form})


	form = CustomUserCreationForm()
	return render(request=request,
				  template_name= "caddecampo/register.html",
				  context={"form":form})


@login_required
def profile(request, id):
	my_user = CustomUser.objects.get(id=id)
	return render(request=request,
				  template_name= "caddecampo/profile.html",
				  context={"my_user":my_user})


@login_required
def editar_register(request, id):
	my_record = CustomUser.objects.get(id=id)

	if request.method == "POST":
		form = CustomUserCreationForm(request.POST, instance=my_record)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			login(request, user)
			messages.info(request, "Usuário Editado com Sucesso!")
			return redirect("/")
		else: 
			for msg in form.error_messages:
				print(form.error_messages[msg])
			return render(request = request,
						  template_name = "caddecampo/register.html",
						  context={"form":form})


	form = CustomUserCreationForm(instance=my_record)
	return render(request=request,
				  template_name= "caddecampo/register.html",
				  context={"form":form})



class register_bk(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'register.html'


def logout_request(request):
	logout(request)
	messages.info(request, "Saiu com Sucesso!")
	return redirect("caddecampo:homepage")


def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request = request,
					template_name = "caddecampo/login.html",
					context={"form":form})


@login_required
def novo_propriedade(request):
	"""Adicionar novo apontamento."""
	
	if request.method == "POST":
		form = CadastroPropriedadeForm(request.POST)#, user=request.user)
		if form.is_valid():
			novo_propriedade = form.save(commit=False)
			novo_propriedade.owner = request.user
			novo_propriedade.save()
			messages.success(request, " Propriedade cadastrada com sucesso!")
			return redirect("/novo_cadastro")
		else: 
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name = "caddecampo/novo_propriedade.html",
						  context={"form":form})


	form = CadastroPropriedadeForm()  #user=request.user)
	return render(request=request,
				  template_name= "caddecampo/novo_propriedade.html",
				  context={"form":form})


@login_required
def editar_propriedade(request, id):
	"""Editar apontamento."""
	my_record = Propriedade.objects.get(id=id, owner=request.user)
	
	if request.method == "POST":
		form = CadastroPropriedadeForm(request.POST, instance=my_record)#, user=request.user)
		if form.is_valid():
			novo_propriedade = form.save(commit=False)
			novo_propriedade.owner = request.user
			novo_propriedade.save()
			messages.success(request, " Propriedade editada com sucesso!")
			return redirect("/")
		else: 
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name = "caddecampo/editar_propriedade.html",
						  context={"form":form})


	form = CadastroPropriedadeForm(instance=my_record)  #user=request.user)
	return render(request=request,
				  template_name= "caddecampo/editar_propriedade.html",
				  context={"id":id, "form":form})


@login_required
def deletar_propriedade(request, id, template_name='caddecampo/deletar_propriedade.html'):
	propriedade= get_object_or_404(Propriedade, id=id)    
	if request.method=='POST':
		propriedade.delete()
		messages.success(request, " Propriedade deletada com sucesso!")
		return redirect("/")
	return render(request, template_name, {'object':propriedade})



@login_required
def novo_area(request):
	"""Adicionar novo apontamento."""
	
	if request.method == "POST":
		form = CadastroAreaForm(request.POST, user=request.user)
		if form.is_valid():
			novo_area = form.save(commit=False)
			#novo_area.owner = request.user
			novo_area.save()
			#user = form.save()
			#username = form.cleaned_data.get('username')
			#messages.success(request, f"Nova Conta Criada: {username}")
			#login(request, user)
			#messages.info(request, f"Você está logado como: {username}")
			messages.success(request, " Área cadastrada com sucesso!")
			return redirect("/novo_cadastro")
		else: 
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name = "caddecampo/novo_area.html",
						  context={"form":form})

	
	form = CadastroAreaForm(user=request.user)
	return render(request=request,
				  template_name= "caddecampo/novo_area.html",
				  context={"form":form})


@login_required
def editar_area(request, id):
	"""Editar apontamento."""
	my_record = Area.objects.get(id=id, propriedade__owner=request.user)
	
	if request.method == "POST":
		form = CadastroAreaForm(request.POST, user=request.user,  instance=my_record)
		if form.is_valid():
			novo_area = form.save(commit=False)
			#novo_area.owner = request.user
			novo_area.save()
			#user = form.save()
			#username = form.cleaned_data.get('username')
			#messages.success(request, f"Nova Conta Criada: {username}")
			#login(request, user)
			#messages.info(request, f"Você está logado como: {username}")
			messages.success(request, " Área editada com sucesso!")
			return redirect("/")
		else: 
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name = "caddecampo/editar_area.html",
						  context={"form":form})

	
	form = CadastroAreaForm(user=request.user,  instance=my_record)
	return render(request=request,
				  template_name= "caddecampo/editar_area.html",
				  context={"id":id, "form":form})


@login_required
def deletar_area(request, id, template_name='caddecampo/deletar_area.html'):
	area= get_object_or_404(Area, id=id, propriedade__owner=request.user)    
	if request.method=='POST':
		area.delete()
		messages.success(request, " Area deletada com sucesso!")
		return redirect("/")
	return render(request, template_name, {'object':area})

@login_required
def desativar_area(request, id, template_name='caddecampo/desativar_area.html'):
	area= get_object_or_404(Area, id=id, propriedade__owner=request.user)    
	if request.method=='POST':
		area.area_ativa = False
		area.area_data_ini_colheita = datetime.now()
		area.save()
		messages.success(request, " Area desativada com sucesso!")
		return redirect("/")
	return render(request, template_name, {'object':area})


@login_required
def novo_adubo(request):
	"""Adicionar novo apontamento."""
	
	if request.method == "POST":
		form = CadastroAduboForm(request.POST)
		if form.is_valid():
			novo_adubo = form.save(commit=False)
			novo_adubo.owner = request.user
			novo_adubo.save()
			messages.success(request, " Adubo cadastrado com sucesso!")
			return redirect("/novo_cadastro")
		else: 
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name = "caddecampo/novo_adubo.html",
						  context={"form":form})


	form = CadastroAduboForm()
	return render(request=request,
				  template_name= "caddecampo/novo_adubo.html",
				  context={"form":form})


@login_required
def novo_defensivo(request):
	"""Adicionar novo apontamento."""
	
	if request.method == "POST":
		form = CadastroDefensivoForm(request.POST)
		if form.is_valid():
			novo_defensivo = form.save(commit=False)
			novo_defensivo.owner = request.user
			novo_defensivo.save()
			messages.success(request, " Defensivo cadastrado com sucesso!")
			return redirect("/novo_cadastro")
		else: 
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name = "caddecampo/novo_defensivo.html",
						  context={"form":form})


	form = CadastroDefensivoForm()
	return render(request=request,
				  template_name= "caddecampo/novo_defensivo.html",
				  context={"form":form})


@login_required
def novo_colheita(request):
	"""Adicionar novo apontamento."""
	if Area.objects.filter(propriedade__owner=request.user, area_ativa=True).exists():
		areas = Area.objects.filter(propriedade__owner=request.user, area_ativa=True)
		if request.method == "POST":
			form = CadastroColheitaForm(request.POST, user=request.user)
			if form.is_valid():
				colheita = form.save(commit=False)
				colheita.colheita_cultura = Area.objects.get(area_nome=colheita.area, propriedade__owner=request.user).area_cultura
				colheita.save()

				messages.success(request, " Colheita adicionada com sucesso!")
				return redirect("/")
			else: 
				for msg in form.error_messages:
					messages.error(request, f"{msg}:{form.error_messages[msg]}")
				return render(request = request,
							  template_name = "caddecampo/novo_colheita.html",
							  context={"form":form})


		form = CadastroColheitaForm(user=request.user)
		return render(request=request,
					  template_name= "caddecampo/novo_colheita.html",
					  context={"areas":areas, "form":form})
	else:
		messages.info(request, " Não existem áreas ativas!")
		return redirect("/")

@login_required
def editar_colheita(request, id):
	"""Adicionar novo apontamento."""
	my_record = Colheita.objects.get(id=id)

	if request.method == "POST":
		form = CadastroColheitaForm(request.POST, instance=my_record, user=request.user)
		if form.is_valid():
			user = form.save()
			#username = form.cleaned_data.get('username')
			#messages.success(request, f"Nova Conta Criada: {username}")
			#login(request, user)
			#messages.info(request, f"Você está logado como: {username}")
			messages.success(request, " Colheita editada com sucesso!")
			return redirect("/")
		else: 
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name = "caddecampo/editar_colheita.html",
						  context={"form":form})


	form = CadastroColheitaForm(instance=my_record, user=request.user)
	return render(request=request,
				  template_name= "caddecampo/editar_colheita.html",
				  context={"id":id, "form":form})



@login_required
def deletar_colheita(request, id, template_name='caddecampo/deletar_colheita.html'):
	colheita= get_object_or_404(Colheita, id=id)    
	if request.method=='POST':
		colheita.delete()
		messages.success(request, " Colheita deletada com sucesso!")
		return redirect("/")
	return render(request, template_name, {'object':colheita})



@login_required
def novo_aplicacao_defensivo(request):
	"""Adicionar novo apontamento."""
	if Area.objects.filter(propriedade__owner=request.user, area_ativa=True).exists():
		areas = Area.objects.filter(propriedade__owner=request.user, area_ativa=True)
		defensivos= Defensivo.objects.filter(owner=request.user)
		if request.method == "POST":
			form = CadastroAplicacaoDefensivoForm(request.POST, user=request.user)
			if form.is_valid():
				user = form.save()
				#username = form.cleaned_data.get('username')
				#messages.success(request, f"Nova Conta Criada: {username}")
				#login(request, user)
				#messages.info(request, f"Você está logado como: {username}")
				messages.success(request, " Aplicação de defensivo adicionado com sucesso!")
				return redirect("/")
			else: 
				for msg in form.error_messages:
					messages.error(request, f"{msg}:{form.error_messages[msg]}")
				return render(request = request,
							  template_name = "caddecampo/novo_aplicacao_defensivo.html",
							  context={"form":form})


		form = CadastroAplicacaoDefensivoForm(user=request.user)
		return render(request=request,
					  template_name= "caddecampo/novo_aplicacao_defensivo.html",
					  context={"areas":areas, "defensivos":defensivos, "form":form})
	else:
		messages.info(request, " Não existem áreas ativas!")
		return redirect("/")

@login_required
def editar_aplicacao_defensivo(request, id):
	"""Editar apontamento."""
	areas = Area.objects.filter(propriedade__owner=request.user, area_ativa=True)
	defensivos= Defensivo.objects.filter(owner=request.user)

	my_record = AplicacaoDefensivo.objects.get(id=id)

	if request.method == "POST":
		form = CadastroAplicacaoDefensivoForm(request.POST, instance=my_record, user=request.user)
		if form.is_valid():
			editar_aplicacao_defensivo = form.save(commit=False)
			editar_aplicacao_defensivo.plantio_slug = "1"
			editar_aplicacao_defensivo.save()
			#messages.info(request, f"Você está logado como: {username}")
			messages.success(request, " Aplicação de defensivo editado com sucesso!")
			return redirect("/")
		else: 
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name = "caddecampo/editar_aplicacao_defensivo.html",
						  context={"form":form})


	form = CadastroAplicacaoDefensivoForm(instance=my_record, user=request.user)
	return render(request=request,
				  template_name= "caddecampo/editar_aplicacao_defensivo.html",
				  context={"id":id,
				  		   "areas":areas,
				  		   "defensivos":defensivos,
						   "form":form})

@login_required
def deletar_aplicacao_defensivo(request, id, template_name='caddecampo/deletar_aplicacao_defensivo.html'):
	aplicacaodefensivo= get_object_or_404(AplicacaoDefensivo, id=id)    
	if request.method=='POST':
		aplicacaodefensivo.delete()
		messages.success(request, " Aplicação de defensivo deletado com sucesso!")
		return redirect("/")
	return render(request, template_name, {'object':aplicacaodefensivo})


@login_required
def novo_aplicacao_adubo(request):
	"""Adicionar novo apontamento."""
	if Area.objects.filter(propriedade__owner=request.user, area_ativa=True).exists():
		areas = Area.objects.filter(propriedade__owner=request.user, area_ativa=True)
		if request.method == "POST":
			form = CadastroAplicacaoAduboForm(request.POST, user=request.user)
			if form.is_valid():
				user = form.save()
				#username = form.cleaned_data.get('username')
				#messages.success(request, f"Nova Conta Criada: {username}")
				#login(request, user)
				#messages.info(request, f"Você está logado como: {username}")
				messages.success(request, " Aplicação de adubo adicionado com sucesso!")
				return redirect("/")
			else: 
				for msg in form.error_messages:
					messages.error(request, f"{msg}:{form.error_messages[msg]}")
				return render(request = request,
							  template_name = "caddecampo/novo_aplicacao_adubo.html",
							  context={"form":form})


		form = CadastroAplicacaoAduboForm(user=request.user)
		return render(request=request,
					  template_name= "caddecampo/novo_aplicacao_adubo.html",
					  context={"areas":areas, "form":form})

	else:
		messages.info(request, " Não existem áreas ativas!")
		return redirect("/")

@login_required
def editar_aplicacao_adubo(request, id):
	"""Editar  apontamento."""
	my_record = AplicacaoAdubo.objects.get(id=id)
	
	if request.method == "POST":
		form = CadastroAplicacaoAduboForm(request.POST, instance=my_record, user=request.user)
		if form.is_valid():
			editar_aplicacao_adubo = form.save(commit=False)
			editar_aplicacao_adubo.plantio_slug = "1"
			editar_aplicacao_adubo.save()
	
			messages.success(request, " Aplicação de adubo editado com sucesso!")
			return redirect("/")
		else: 
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
			return render(request = request,
						  template_name = "caddecampo/editar_aplicacao_adubo.html",
						  context={ "form":form})


	form = CadastroAplicacaoAduboForm(instance=my_record, user=request.user)
	return render(request=request,
				  template_name= "caddecampo/editar_aplicacao_adubo.html",
				  context={"id":id, "form":form})


@login_required
def deletar_aplicacao_adubo(request, id, template_name='caddecampo/deletar_aplicacao_adubo.html'):
	aplicacaoadubo= get_object_or_404(AplicacaoAdubo, id=id)    
	if request.method=='POST':
		aplicacaoadubo.delete()
		messages.success(request, " Aplicação de adubo deletado com sucesso!")
		return redirect("/")
	return render(request, template_name, {'object':aplicacaoadubo})




@login_required
def relatorios_bck(request):
	#return HttpResponse("Woe this is an <strong> awesome</strong> tuotorial")
	return render(request=request,
				  template_name="caddecampo/relatorio.html",
				  context={"propriedades": Propriedade.objects.all(),
						   "areas": Area.objects.all(),
						   "defensivos": AplicacaoDefensivo.objects.all(),
						   "adubos": AplicacaoAdubo.objects.all(),
						   "colheitas": Colheita.objects.all()})

@login_required
def relatorios(request):
	return render(request=request,
				  template_name="caddecampo/relatorio.html",
				  context={"propriedades": Propriedade.objects.filter(owner=request.user)})


@login_required
def insumos(request):
	#defensivos = Defensivo.objects.filter(owner=request.user)
	#adubos = Adubo.objects.filter(owner=request.user)
	return render(request=request,
				  template_name="caddecampo/insumos.html",
				  context={"defensivos": Defensivo.objects.filter(owner=request.user),
						   "adubos": Adubo.objects.filter(owner=request.user)
						   })



@login_required
def deletar_adubo(request, id, template_name='caddecampo/deletar_adubo.html'):
	adubo= get_object_or_404(Adubo, id=id)    
	if request.method=='POST':
		adubo.delete()
		messages.success(request, " Adubo deletado com sucesso!")
		return redirect("/insumos")
	return render(request, template_name, {'object':adubo})


@login_required
def deletar_defensivo(request, id, template_name='caddecampo/deletar_defensivo.html'):
	defensivo = get_object_or_404(Defensivo, id=id)    
	if request.method=='POST':
		defensivo.delete()
		messages.success(request, " Defensivo deletado com sucesso!")
		return redirect("/insumos")
	return render(request, template_name, {'object':defensivo})


@login_required
def single_slug(request, single_slug):
	propriedades = [p.slug for p in Propriedade.objects.filter(owner=request.user)]

	if single_slug in propriedades:
		#return HttpResponse(f"{single_slug} is in propriedades")
		areas_pertencentes = Area.objects.filter(propriedade__slug=single_slug)
		nome = Propriedade.objects.get(slug=single_slug).propriedade_nome

		return render(request,
					  "caddecampo/areas.html",
					  {"areas": areas_pertencentes,
					  "nome": nome})
	
	areas = [ar.slug for ar in Area.objects.filter(propriedade__owner=request.user)]


	if single_slug in areas:
		dfs_pertencentes = AplicacaoDefensivo.objects.filter(area__slug=single_slug)
		ads_pertencentes = AplicacaoAdubo.objects.filter(area__slug=single_slug)
		cls_pertencentes = Colheita.objects.filter(area__slug=single_slug)
		nome = Area.objects.get(slug=single_slug).area_nome
		data_plantiu = Area.objects.get(slug=single_slug).area_data_plantiu
		tamanho = Area.objects.get(slug=single_slug).area_tamanho 
		situacao = Area.objects.get(slug=single_slug).area_ativa

		for dfs in dfs_pertencentes:
			dfs.defensivo_volume_he = int(dfs.defensivo_volume * 10000 / tamanho)
			dfs.save()

		for ads in ads_pertencentes:
			ads.adubo_dosagem_he = int(ads.adubo_dosagem * 10000 / tamanho)
			ads.save()

		return render(request,
					  "caddecampo/area.html",
					  {"defensivos": dfs_pertencentes,
					  "adubos": ads_pertencentes,
					  "colheitas": cls_pertencentes,
					  "nome": nome,
					  "situacao":situacao,
					  "data_plantiu":data_plantiu,
					  "tamanho":tamanho,
					  "single_slug":single_slug})
	
	

	return HttpResponse(f"{single_slug} nao encontrado")



@login_required
def generate_pdf(request, single_slug, *args, **kwargs):
	usuario_nome = request.user.usuario_nome
	usuario_cpf = request.user.usuario_cpf
	usuario_ie = request.user.usuario_ie
	usuario_cidade = request.user.usuario_cidade

	areas = [ar.slug for ar in Area.objects.filter(propriedade__owner=request.user)]


	if single_slug in areas:
		dfs_pertencentes = AplicacaoDefensivo.objects.filter(area__slug=single_slug)
		ads_pertencentes = AplicacaoAdubo.objects.filter(area__slug=single_slug)
		cls_pertencentes = Colheita.objects.filter(area__slug=single_slug)
		propriedade = Area.objects.get(slug=single_slug).propriedade
		localizacao = Propriedade.objects.get(owner=request.user, propriedade_nome=propriedade).propriedade_summary
		nome = Area.objects.get(slug=single_slug).area_nome
		data_plantiu = Area.objects.get(slug=single_slug).area_data_plantiu
		data_plantiu_fim = Area.objects.get(slug=single_slug).area_data_plantiu_fim
		n_plantas = Area.objects.get(slug=single_slug).area_nplantas
		tamanho =  Area.objects.get(slug=single_slug).area_tamanho
		cultura = Area.objects.get(slug=single_slug).area_cultura
		unidade = 'Kg'
		colheita_total = 0
		def_solid_total = 0
		def_liqui_total = 0
		def_solid_planta = 0
		def_liqui_planta = 0
		adubo_total = 0
		adubo_planta = 0

		for col in cls_pertencentes:
			colheita_total += col.colheita_quantia
			unidade = col.colheita_unidade

		for dfs in dfs_pertencentes:
			try:
				formulacao = Defensivo.objects.get(defensivo_nome=dfs.defensivo_nome).defensivo_formulacao
				#print(formulacao)
			except:
				formulacao = 'Solido'

			if formulacao == "Solido":
				def_solid_total += (dfs.defensivo_dosagem * dfs.defensivo_volume)/100
				#print(def_solid_total)
			else:
				def_liqui_total += (dfs.defensivo_dosagem * dfs.defensivo_volume)/100
				#print(def_liqui_total)


		for ads in ads_pertencentes:
			adubo_total += ads.adubo_dosagem


		adubo_planta = round(adubo_total / n_plantas, 3)
		unides_p_planta = round(colheita_total / n_plantas, 3)
		def_solid_planta = round(def_solid_total / n_plantas, 3)
		def_liqui_planta = round(def_liqui_total / n_plantas, 3)

	data = {
			"usuario_nome": usuario_nome,
			"usuario_cpf": usuario_cpf,
			"usuario_ie": usuario_ie,
			"usuario_cidade": usuario_cidade,
			"n_plantas": n_plantas,
			"defensivos": dfs_pertencentes,
			"adubos": ads_pertencentes,
			"colheitas": cls_pertencentes,
			"localizacao": localizacao,
			"data": data_plantiu,
			"data_fim": data_plantiu_fim,
			"nome": nome,
			"colheita_total": colheita_total,
			"unidade": unidade,
			"unides_p_planta": unides_p_planta,
			"def_solid_planta": def_solid_planta,
			"def_liqui_planta": def_liqui_planta,
			"adubo_planta": adubo_planta,
			"tamanho": tamanho,
			"cultura": cultura
	}
	pdf = render_to_pdf('caddecampo/pdf.html', data)
	return HttpResponse(pdf, content_type='application/pdf')