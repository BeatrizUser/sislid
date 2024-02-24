from django.contrib import admin
from .models import Lideranca, Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bairro', 'lideranca')
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

admin.site.register(Lideranca)
admin.site.register(Pessoa, PessoaAdmin)
