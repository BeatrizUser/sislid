import json
import os
import requests
from django.contrib import admin
from django.conf import settings
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import *

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bairro', 'lideranca', 'zona_eleitoral', 'secao_eleitoral', 'validar_titulo')
    fieldsets = (
        (None, {
            'fields': ('nome', 'sexo', 'idade', 'lideranca')
        }),
        ('Título Eleitoral', {
            'fields': ('titulo_eleitor', 'nome_mae', 'nao_consta', 'zona_eleitoral', 'secao_eleitoral'),
        }),
        ('Endereço', {
            'fields': ('rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep'),
        }),
    )
    search_fields = ['lideranca__nome'] 

    def validar_titulo(self, obj):
        if obj.zona_eleitoral and obj.secao_eleitoral:
            local, _, _, _ = preencher_local_de_votacao_cached(int(obj.zona_eleitoral), int(obj.secao_eleitoral))
            if local:
                return local
            else:
                return "Local de votação não encontrado"
        else:
            return "Zona e/ou seção eleitoral não informadas"

    validar_titulo.short_description = 'Local de Votação'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('lideranca')  # Otimização para evitar queries adicionais

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
    list_display = ['nome', 'bairro_de_atuacao', 'contato', 'exibir_foto']

    def exibir_foto(self, obj):
        if obj.foto:
            foto_url = settings.MEDIA_URL + str(obj.foto)
            return format_html('<img src="{}" style="height: 50px; width: 50px;" />', foto_url)
        else:
            return 'Sem foto'

    exibir_foto.short_description = 'Foto'


admin.site.register(Lideranca, LiderancaAdmin)
admin.site.register(Pessoa, PessoaAdmin)
