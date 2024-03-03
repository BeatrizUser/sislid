from django.contrib import admin
from .models import *

# Register your models here.
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'tipo', 'mensagem', 'formatted_date_time']

    def formatted_date_time(self, obj):
        return obj.data_hora_envio.strftime('%d/%m/%Y - %H:%M')

    formatted_date_time.short_description = 'Data e Hora de Envio'

admin.site.register(Pergunta, PerguntaAdmin)