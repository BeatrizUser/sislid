from django.db import models
from cadastro.choices import *

class Pergunta(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=OPCOES)
    mensagem = models.TextField()
    data_hora_envio = models.DateTimeField(auto_now_add=True)
    bairro_sao_goncalo = models.CharField(max_length=100, choices=BAIRROS_SAO_GONCALO)

    def short_date_time_format(self):
        return self.data_hora_envio.strftime('%d/%m/%Y - %H:%M')

    def __str__(self):
        return self.nome