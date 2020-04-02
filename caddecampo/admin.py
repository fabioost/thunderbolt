from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Propriedade, Area, Adubo, Defensivo, Colheita, AplicacaoDefensivo, AplicacaoAdubo
from users.models import CustomUser
from tinymce.widgets import TinyMCE

#from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
#overriding
#class CustomUserAdmin(UserAdmin):
	#add_form = CustomUserCreationForm
	#form = CustomUserChangeForm
	#model = CustomUser
	#list_display = ['email', 'username',]

admin.site.site_header = 'Caderno de campo'
#admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Propriedade)
admin.site.register(Area)
#admin.site.register(Cultura)
#admin.site.register(Apontamento)
admin.site.register(Adubo)
admin.site.register(Defensivo)
admin.site.register(Colheita)
admin.site.register(AplicacaoAdubo)
admin.site.register(AplicacaoDefensivo)
