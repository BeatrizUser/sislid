from django.contrib import admin
from django.utils.safestring import mark_safe
from .utils import preencher_local_de_votacao
from .models import Pessoa, Pergunta, Lideranca

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
            local, _, _, _ = preencher_local_de_votacao(int(obj.zona_eleitoral), int(obj.secao_eleitoral))
            if local:
                return local
            else:
                return "Local de votação não encontrado"
        else:
            return "Zona e/ou seção eleitoral não informadas"

    validar_titulo.short_description = 'Local de Votação'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('lideranca')  # Otimização para evitar queries adicionais

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'tipo', 'mensagem', 'formatted_date_time']

    def formatted_date_time(self, obj):
        return obj.data_hora_envio.strftime('%d/%m/%Y - %H:%M')

    formatted_date_time.short_description = 'Data e Hora de Envio'

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Lideranca)
admin.site.register(Pessoa, PessoaAdmin)

