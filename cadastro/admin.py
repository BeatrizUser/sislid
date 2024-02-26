from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import *

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bairro', 'lideranca','zona_eleitoral', 'validar_titulo')
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
        url = f"https://www.tse.jus.br/servicos-eleitorais/titulo-e-local-de-votacao/titulo-e-local-de-votacao"
        return mark_safe(f'<a class="btn btn-success" href="{url}" target="_blank"><i class="fas fa-users mr-2"></i> Validar título eleitoral</a>')

    validar_titulo.short_description = 'Validar título eleitoral'

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'tipo', 'mensagem', 'formatted_date_time']

    def formatted_date_time(self, obj):
        return obj.data_hora_envio.strftime('%d/%m/%Y - %H:%M')

    formatted_date_time.short_description = 'Data e Hora de Envio'

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Lideranca)
admin.site.register(Pessoa, PessoaAdmin)
