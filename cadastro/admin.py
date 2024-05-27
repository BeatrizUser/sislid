import json
import os
import requests
from django.contrib import admin
from django.conf import settings
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Lideranca, Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('criado_por', 'nome', 'data_de_nascimento', 'calcular_idade','genero', 'telefone', 'whatsapp', 'bairro', 'lideranca', 'zona_eleitoral', 'secao_eleitoral', 'apto_a_votar', 'votante', 'filhos', 'grau_de_influencia', 'validar_titulo')
    fieldsets = (
        ('Dados Cadastrais', {
            'fields': ('nome', 'data_de_nascimento', 'genero', 'telefone', 'whatsapp', 'email', 'lideranca')
        }),
        ('Título Eleitoral', {
            'fields': ('titulo_eleitor', 'nome_mae', 'nao_consta', 'zona_eleitoral', 'secao_eleitoral', 'local_de_votacao', 'apto_a_votar', 'votante'),
        }),
        ('Endereço', {
            'fields': ('rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep'),
        }),
        ('Outros', {
            'fields': ('filhos', 'grau_de_influencia'),
        }),
    )
    search_fields = ['nome'] 

    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related('lideranca')
        if request.user.has_perm('cadastro.can_view_own_pessoa'):
            return qs.filter(criado_por=request.user)
        if request.user.is_superuser:
            return qs  # Retorna todos os objetos
        return qs

    def validar_titulo(self, obj):
        if obj.zona_eleitoral is not None and obj.secao_eleitoral is not None:
            if obj.zona_eleitoral.isdigit() and obj.secao_eleitoral.isdigit():
                local, _, _, _ = preencher_local_de_votacao_cached(int(obj.zona_eleitoral), int(obj.secao_eleitoral))
                if local:
                    return local
                else:
                    return "Local de votação não encontrado"
            else:
                return "Zona e/ou seção eleitoral não informadas"
        else:
            return "Zona e/ou seção eleitoral não informadas"

    validar_titulo.short_description = 'Local de Votação'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        super().save_model(request, obj, form, change)

def preencher_local_de_votacao_cached(zona, secao):
    CACHE_FILE = "locais.json"
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as file:
                locais_votacao = json.load(file)
        else:
            # Se o arquivo de cache não existir, faz uma solicitação à API e salva os dados no cache
            url = f"https://apps.tre-rj.jus.br/api-dados-abertos/locaisvotacao/municipio/S%C3%A3o%20Gon%C3%A7alo"
            response = requests.get(url)
            response.raise_for_status()  # Verifica se houve erro na requisição
            locais_votacao = response.json()
            with open(CACHE_FILE, "w") as file:
                json.dump(locais_votacao, file)

        # Procura o local de votação na lista de locais obtidos do cache
        for local in locais_votacao:
            secoes = local["secoes"].split(",")
            if str(secao) in secoes and int(local["numZona"]) == zona:
                return local["local"], local["endereco"], local["bairro"], local["cep"]

    except Exception as e:
        print(f"Erro ao buscar locais de votação: {e}")

    return None, None, None, None

class LiderancaAdmin(admin.ModelAdmin):
    list_display = ['exibir_foto', 'nome', 'bairro_de_atuacao', 'telefone_whatsapp', 'tipo_de_atuacao', 'acordo_link']
    readonly_fields = ['acordo_link']
    
    def acordo_link(self, obj):
        if obj.acordo:
            return format_html('<a href="{}" target="_blank">Visualizar</a>', obj.acordo.url)
        else:
            return '-'

    acordo_link.short_description = 'Acordo'

    def exibir_foto(self, obj):
        if obj.foto:
            foto_url = settings.MEDIA_URL + str(obj.foto)
            return format_html('<img src="{}" style="height: 50px; width: 50px;" />', foto_url)
        else:
            return 'Sem foto'

    exibir_foto.short_description = 'Foto'

admin.site.register(Lideranca, LiderancaAdmin)
admin.site.register(Pessoa, PessoaAdmin)
