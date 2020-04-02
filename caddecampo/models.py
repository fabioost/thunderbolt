from django import forms
from django.db import models
from datetime import datetime 
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.utils.text import slugify



class Propriedade(models.Model):
	propriedade_nome = models.CharField(max_length=50)
	propriedade_summary = models.CharField(max_length=50) #localizacao
	propriedade_ativa = models.BooleanField(default=True)
	proriedade_slug = models.CharField(max_length=50, default=1) 
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.propriedade_nome)
		super(Propriedade, self).save(*args, **kwargs)

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Propriedades"

	def __str__(self):
		return self.propriedade_nome

class Area(models.Model):
	area_data_plantiu = models.DateField(default=datetime.now) #inicio do plantio
	area_data_plantiu_fim = models.DateField(default=datetime.now) #fim do plantio
	area_nome = models.CharField(max_length=50)
	area_tamanho = models.IntegerField()
	area_nplantas = models.IntegerField()
	area_cultura = models.CharField(max_length=50)
	area_data_ini_colheita = models.DateField(default=datetime.now) #Data do desativamento
	area_summary = models.CharField(max_length=50, default='non')
	area_ativa = models.BooleanField(default=True)
	area_slug = models.CharField(max_length=50, default=1)
	propriedade = models.ForeignKey(Propriedade, default=1, verbose_name="Propriedade", on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.area_nome + str(self.area_data_plantiu))
		super(Area, self).save(*args, **kwargs)

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Areas"

	def __str__(self):
		return self.area_nome 
		


class AplicacaoAdubo(models.Model):
	apontamento_published = models.DateField(default=datetime.now)
	adubo_nome = models.CharField(max_length=30)
	adubo_dosagem = models.IntegerField()
	adubo_dosagem_he = models.IntegerField(default=1)
	plantio_slug = models.CharField(max_length=30, default=1)
	area = models.ForeignKey(Area, default=1, verbose_name="Apontamento plantio", on_delete=models.CASCADE)
	#slug = models.SlugField(unique=True)

	#def save(self, *args, **kwargs):
		#self.slug = slugify(self.apontamento_published)
		#super(AplicacaoAdubo, self).save(*args, **kwargs)

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Adubações"



class AplicacaoDefensivo(models.Model):
	apontamento_published = models.DateField(default=datetime.now)
	defensivo_nome = models.CharField(max_length=30)
	defensivo_dosagem = models.IntegerField()
	defensivo_volume = models.IntegerField() 
	defensivo_volume_he = models.IntegerField(default=1)#litros por hectare
	defensivo_praga = models.CharField(max_length=30)
	defensivo_intervalo = models.IntegerField(default=1)
	plantio_slug = models.CharField(max_length=30, default=1)
	area = models.ForeignKey(Area, default=1, verbose_name="Apontamento plantio", on_delete=models.CASCADE)
	#slug = models.SlugField(unique=True)

	#def save(self, *args, **kwargs):
		#self.slug = slugify(self.apontamento_published)
		#super(AplicacaoDefensivo, self).save(*args, **kwargs)

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Pulverizações"



class Adubo(models.Model):
	CLASS_CHOICES = (
		('Foliar','Foliar'),
		('Nao Foliar','Nao Foliar')
	)
	COMP_CHOICES = (
		('Organico','Organico'),
		('Sintetico','Sintetico')
	)

	adubo_nome = models.CharField(max_length=30)
	adubo_classificacao = models.CharField(max_length=30, choices = CLASS_CHOICES) #foliar naofoliar
	adubo_composicao = models.CharField(max_length=20, choices = COMP_CHOICES) # organico sintetico
	adubo_summary = models.CharField(max_length=20, default='non')
	adubo_slug = models.CharField(max_length=20, default=1)
	#propriedade = models.ForeignKey(Propriedade, default=1, verbose_name="Propriedade", on_delete=models.CASCADE)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Adubos"

	def __str__(self):
		return self.adubo_nome



class Defensivo(models.Model):
	CLASS_CHOICES = (
		('Acaricida','Acaricida'),
		('Bactericida','Bactericida'),
		('Fungicida','Fungicida'),
		('Herbicida','Herbicida'),
		('Inceticida','Inceticida'),
		('Nematicida','Nematicida'),
		('Biologico','Biologico')	
	)
	COMP_CHOICES = (
		('Liquido','Liquido'),
		('Solido','Solido')
	)
	defensivo_nome = models.CharField(max_length=20)
	defensivo_classificacao = models.CharField(max_length=20, choices = CLASS_CHOICES)
	defensivo_formulacao = models.CharField(max_length=20, choices = COMP_CHOICES) #liquido solido
	#defensivo_limitereentradas = models.CharField(max_length=20) #dias
	defensivo_reentrada = models.IntegerField(default=1)  #dias
	defensivo_dosagem = models.IntegerField(default=30)
	defensivo_principiosativos = models.CharField(max_length=20)
	defensivo_indicacoes = models.CharField(max_length=20)
	defensivo_summary = models.CharField(max_length=20, default='non')
	defensivo_slug = models.CharField(max_length=20, default=1)
	#propriedade = models.ForeignKey(Propriedade, default=1, verbose_name="Propriedade", on_delete=models.CASCADE)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Defensivos"

	def __str__(self):
		return self.defensivo_nome

class Colheita(models.Model):
	CLASS_CHOICES = (
		('kg','kg'),
		('Caixas','Caixas'),
		('Unid','Unid')
	)
	apontamento_published = models.DateField(default=datetime.now)
	colheita_cultura = models.CharField(max_length=20, default='non')
	colheita_quantia = models.IntegerField()
	colheita_unidade = models.CharField(max_length=20, default='Kg', choices = CLASS_CHOICES)
	colheita_slug = models.CharField(max_length=20, default=1)
	#slug = models.SlugField(prepopulate_from=('apontamento_published',))
	area = models.ForeignKey(Area, default=1, verbose_name="Area colheita", on_delete=models.CASCADE)
	#slug = models.SlugField(unique=True)

	#def save(self, *args, **kwargs):
		#self.slug = slugify(self.apontamento_published)
		#super(Colheita, self).save(*args, **kwargs)


	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Colheitas"

	

