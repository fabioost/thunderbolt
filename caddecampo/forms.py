from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.contrib.auth.models import User

#from django.forms.models import modelformset_factory
from .models import  Adubo, Defensivo, Colheita, AplicacaoDefensivo, AplicacaoAdubo, Area, Propriedade
from users.models import CustomUser
#from .models import CustomUser
from .validators import validate_docaddecampo_email, isCpfValid



class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField()
	usuario_cpf = forms.CharField(validators=[isCpfValid])

	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'usuario_nome', 'usuario_cpf', 'usuario_fone', 'usuario_ie', 'usuario_endereço', 'usuario_bairro', 'usuario_cidade', 'usuario_estado', 'usuario_cep')
		labels = {'username':'Usuário', 'email': 'Email','usuario_nome':'Nome Completo', 'usuario_endereço':'Endereço', 'usuario_bairro':'Bairro', 'usuario_cidade':'Cidade', 'usuario_estado':'Estado', 'usuario_cep':'CEP','usuario_cpf':'CPF', 'usuario_fone':'Fone', 'usuario_ie':'Incrição Estadual'}
		

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields
		#exclude = ('usuario_info',)




class DateInputs(forms.DateInput):
	input_type = 'date'
	



class CadastroPropriedadeForm(forms.ModelForm):
	#def __init__(self, *args, **kwargs):
		#user = kwargs.pop('user')
		#super(CadastroPropriedadeForm, self).__init__(*args, **kwargs)
		#self.fields['lists'].queryset = List.objects.filter(user=user)

	#lists = forms.ModelChoiceField(queryset=None, widget=forms.Select, required=True)
	#cultura = forms.ModelChoiceField(queryset=Cultura.objects.all())

	class Meta:
		
		model = Propriedade
		fields = ['propriedade_nome','propriedade_summary']
		labels = {'propriedade_nome':'Nome da Propriedade:<br>(Exp.: Hortifruti do Fritz)', 'propriedade_summary': 'Localização:<br>(Coordenadas Geográficas)'}
		widgets = {
				   'text': forms.Textarea(attrs={'cols': 80}),
				   'text': forms.Textarea(attrs={'cols': 80}),
		}


class CadastroAreaForm(forms.ModelForm):
	#area_data_plantiu = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickSeconds": False}))

	#propriedade = forms.ModelChoiceField(queryset=Propriedade.objects.filter(owner=request.user))

	class Meta:
		
		model = Area
		fields = ['area_data_plantiu', 'area_data_plantiu_fim', 'area_nome','area_tamanho','area_cultura', 'area_nplantas', 'propriedade']
		labels = {'area_data_plantiu':'Data do Início do Plantio','area_data_plantiu_fim':'Data do Fim do Plantio','area_nome':'Nome da área:<br>(Exp.: Estufa 1)','area_tamanho':'Tamanho da área:<br>(em metros quadrados)','area_cultura':'Cultura', 'area_nplantas':'Número de Plantas','propriedade': 'Propriedade'}
		widgets = {
				   'Data': DateInputs(),
				   'text': forms.Textarea(attrs={'cols': 80}),
				   'text' : forms.Textarea(attrs={'cols': 80}),
				   'text' : forms.Textarea(attrs={'cols': 80}),
				   'Data': DateInputs(),
				   'role' : forms.Textarea(attrs={'cols': 80})
		}

	def __init__(self, *args, **kwargs):
			self.user = kwargs.pop('user', None)
			super(CadastroAreaForm, self).__init__(*args, **kwargs)
			#print(self.user)
			self.fields['propriedade'].queryset = Propriedade.objects.filter(owner=self.user)

	


class CadastroAduboForm(forms.ModelForm):

	#cultura = forms.ModelChoiceField(queryset=Cultura.objects.all())

	class Meta:
		
		model = Adubo
		fields = ['adubo_nome','adubo_classificacao','adubo_composicao']
		labels = {'adubo_nome':'Nome do Adubo', 'adubo_classificacao': 'Classificação', 'adubo_composicao':'Composicao'}
		widgets = {
				   'text': forms.Textarea(attrs={'cols': 80}),
				   'role' : forms.Textarea(attrs={'cols': 80}),
				   'role' : forms.Textarea(attrs={'cols': 80})
		}


class CadastroDefensivoForm(forms.ModelForm):

	#cultura = forms.ModelChoiceField(queryset=Cultura.objects.all())

	class Meta:
		
		model = Defensivo
		fields = ['defensivo_nome','defensivo_classificacao','defensivo_formulacao', 'defensivo_dosagem', 'defensivo_reentrada']
		labels = {'defensivo_nome':'Nome do defensivo', 'defensivo_classificacao': 'Classificação', 'defensivo_formulacao':'Formulação', 'defensivo_dosagem':'Dosagem Padrão(g/ml) por 100L',
		'defensivo_reentrada':'Intervalo de reentrada em dias',}
		widgets = {
				   'text': forms.Textarea(attrs={'cols': 80}),
				   'role' : forms.Textarea(attrs={'cols': 80}),
				   'role' : forms.Textarea(attrs={'cols': 80}),
				   'role' : forms.Textarea(attrs={'cols': 80})
		}

class CadastroColheitaForm(forms.ModelForm):

	#cultura = forms.ModelChoiceField(queryset=Cultura.objects.all())

	class Meta:
		
		model = Colheita
		fields = ['apontamento_published','colheita_quantia','colheita_unidade','area']
		labels = {'apontamento_published':'DATA','colheita_quantia':'Quantidade', 'colheita_unidade': 'Unidade', 'area':'Área'}
		widgets = {
				   'Data': DateInputs(),
				   'text': forms.Textarea(attrs={'cols': 80}),
				   'role' : forms.Textarea(attrs={'cols': 80}),
				   'role' : forms.Textarea(attrs={'cols': 80})
		}

	def __init__(self, *args, **kwargs):
			self.user = kwargs.pop('user', None)
			super(CadastroColheitaForm, self).__init__(*args, **kwargs)
			self.fields['area'] = forms.ModelChoiceField(label='Área', empty_label='Selecione', queryset=Area.objects.filter(propriedade__owner=self.user, area_ativa=True),
										widget=forms.Select(attrs={'class': 'form-control'}))


class CadastroAplicacaoDefensivoForm(forms.ModelForm):

	#defensivo_nome = forms.ModelChoiceField(label='Defensivos',empty_label='Selecione', queryset=Defensivo.objects.all(),
										#widget=forms.Select(attrs={'class': 'form-control'}))								
	class Meta:
		model = AplicacaoDefensivo
		#exclude = ('plantio_slug',)
		fields = ['apontamento_published', 'defensivo_nome', 'defensivo_dosagem', 'defensivo_volume', 'defensivo_praga', 'defensivo_intervalo','area']
		

		labels = {
			'apontamento_published':'DATA',
			'defensivo_nome': 'Defensivo',
			'defensivo_dosagem': 'Dosagem de aplicação <br> (g ou mL/100L)',
			'defensivo_volume': 'Volume de calda (L)',
			'defensivo_praga': 'Praga',
			'defensivo_intervalo': 'Carência (dias)',
			'area':'Área'
		}

	def __init__(self, *args, **kwargs):
			self.user = kwargs.pop('user', None)
			super(CadastroAplicacaoDefensivoForm, self).__init__(*args, **kwargs)
			#print(self.user.id)
			#self.fields['defensivo_nome'].queryset = Defensivo.objects.filter(owner=self.user)
			self.fields['defensivo_nome'] = forms.ModelChoiceField(label='Defensivo', empty_label='Selecione', queryset=Defensivo.objects.filter(owner=self.user),
										widget=forms.Select(attrs={'class': 'form-control'}))
			self.fields['area'] = forms.ModelChoiceField(label='Área', empty_label='Selecione', queryset=Area.objects.filter(propriedade__owner=self.user, area_ativa=True),
										widget=forms.Select(attrs={'class': 'form-control'}))

			


class CadastroAplicacaoAduboForm(forms.ModelForm):

	#adubo_nome = forms.ModelChoiceField(queryset=Adubo.objects.all())

	class Meta:
		
		model = AplicacaoAdubo
		fields = ['apontamento_published','adubo_nome','adubo_dosagem','area']
		labels = {'apontamento_published':'DATA','adubo_nome':'Nome do adubo', 'adubo_dosagem': 'Quantidade(kg)', 'area':'Área'}
		widgets = {
				   'Data': DateInputs(),
				   'text': forms.Textarea(attrs={'cols': 80}),
				   'role' : forms.Textarea(attrs={'cols': 80}),
				   'role' : forms.Textarea(attrs={'cols': 80})
		}

	def __init__(self, *args, **kwargs):
			self.user = kwargs.pop('user', None)
			super(CadastroAplicacaoAduboForm, self).__init__(*args, **kwargs)
			#print(self.user)
			self.fields['adubo_nome'] = forms.ModelChoiceField(label='Adubo', empty_label='Selecione', queryset=Adubo.objects.filter(owner=self.user),
										widget=forms.Select(attrs={'class': 'form-control'}))
			self.fields['area'] = forms.ModelChoiceField(label='Área', empty_label='Selecione', queryset=Area.objects.filter(propriedade__owner=self.user, area_ativa=True),
										widget=forms.Select(attrs={'class': 'form-control'}))


