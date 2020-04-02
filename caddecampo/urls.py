
from django.contrib import admin
from django.urls import path, include
from . import views

app_name= "caddecampo"

urlpatterns = [
    path("home",views.homepage, name="homepage"),
    path('admin/', admin.site.urls),
    path("register/", views.register, name="register"),
    path("editar_register/<id>", views.editar_register, name="editar_register"),
    path("profile/<id>", views.profile, name="profile"),
    path("logout/", views.logout_request, name="logout"),
    path("novo_apontamento/<id>", views.novo_apontamento, name="novo_apontamento"),
    path("novo_cadastro/", views.novo_cadastro, name="novo_cadastro"),
    path("novo_propriedade/", views.novo_propriedade, name="novo_propriedade"),
    path("editar_propriedade/<id>", views.editar_propriedade, name="editar_propriedade"),
    path("deletar_propriedade/<id>", views.deletar_propriedade, name="deletar_propriedade"),
    path("novo_area/", views.novo_area, name="novo_area"),
    path("editar_area/<id>", views.editar_area, name="editar_area"),
    path("deletar_area/<id>", views.deletar_area, name="deletar_area"),
    path("desativar_area/<id>", views.desativar_area, name="desativat_area"),
    path("novo_adubo/", views.novo_adubo, name="novo_adubo"),
    path("novo_defensivo/", views.novo_defensivo, name="novo_defensivo"),
    path("novo_colheita/", views.novo_colheita, name="novo_colheita"),
    path("editar_colheita/<id>", views.editar_colheita, name="editar_colheita"),
    path("deletar_colheita/<id>", views.deletar_colheita, name="deletar_colheita"),
    path("novo_aplicacao_defensivo/", views.novo_aplicacao_defensivo, name="novo_aplicacao_defensivo"),
    path("editar_aplicacao_defensivo/<id>", views.editar_aplicacao_defensivo, name="editar_aplicacao_defensivo"),
    path("deletar_aplicacao_defensivo/<id>", views.deletar_aplicacao_defensivo, name="deletar_aplicacao_defensivo"),
    path("novo_aplicacao_adubo/", views.novo_aplicacao_adubo, name="novo_aplicacao_adubo"),
    path("editar_aplicacao_adubo/<id>", views.editar_aplicacao_adubo, name="editar_aplicacao_adubo"),
    path("deletar_aplicacao_adubo/<id>", views.deletar_aplicacao_adubo, name="deletar_aplicacao_adubo"),
    path("cad_sucess/", views.cad_sucesso, name="cad_sucesso"),
    path("cad_editar_sucess/", views.cad_editar_sucesso, name="cad_editar_sucesso"),
    #path("user_cad_sucess/", views.user_cad_sucesso, name="user_cad_sucesso"),
    path("apt_sucess/", views.apt_sucesso, name="apt_sucesso"),
    path("deletar_sucess/", views.deletar_sucess, name="deletar_sucess"),
    path("editar_sucess/", views.editar_sucesso, name="editar_sucesso"),
    path("relatorio/", views.relatorios, name="relatorios"),
    path("insumos/", views.insumos, name="insumos"),
    path("deletar_adubo/<id>", views.deletar_adubo, name="deletar_adubo"),
    path("deletar_defensivo/<id>", views.deletar_defensivo, name="deletar_defensivo"),
    path("desenvolvedor/", views.desenvolvedor, name="desenvolvedor"),

    path("pdf/<single_slug>/",views.generate_pdf, name="generate_pdf"),

    path("<single_slug>/", views.single_slug, name="slug"),
  
]