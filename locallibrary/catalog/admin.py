from django.contrib import admin
from .models import Autor,Auxiliar, Avaliador, AvaliarProjeto, Premio, EnviarProjeto


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_filter = ('id', 'nome')


@admin.register(Auxiliar)
class AuxiliarAdmin(admin.ModelAdmin):
    list_filter = ('id', 'nome')


@admin.register(EnviarProjeto)
class EnviarProjetoAdmin(admin.ModelAdmin):
    list_filter = ('id', 'area','titulo','dataEnvio')


@admin.register(Avaliador)
class AvaliadorAdmin(admin.ModelAdmin):
    list_filter = ('id', 'nome')


@admin.register(AvaliarProjeto)
class AvaliarProjetoAdmin(admin.ModelAdmin):
    list_filter = ('id', 'avaliador')


@admin.register(Premio)
class PremioAdmin(admin.ModelAdmin):
    list_filter = ('id', 'nome', 'descricao')

# Register your models here.
