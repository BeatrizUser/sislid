from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from cadastro.choices import *
import requests
import re

class Lideranca(models.Model):
    nome = models.CharField(max_length=100)
    bairro_de_atuacao = models.CharField(max_length=100, choices=BAIRROS_SAO_GONCALO)
    contato = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='liderancas/', blank=True, null=True)

    def __str__(self):
        return self.nome

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

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    rua = models.CharField(max_length=255, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    idade = models.IntegerField(blank=True, null=True)
    titulo_eleitor = models.CharField(max_length=20, unique=True)
    zona_eleitoral = models.CharField(max_length=10, blank=True, null=True)
    secao_eleitoral = models.CharField(max_length=10, blank=True, null=True)
    local_de_votacao = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    nao_consta = models.BooleanField(default=False)
    lideranca = models.ForeignKey(Lideranca, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        # Removida a necessidade de buscar a liderança pelo ID antes de salvar
        super(Pessoa, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.lideranca.nome}" if self.lideranca else self.nome

    def pesquisar_cep(self):
        cep = re.sub(r'\D', '', self.cep)
        if len(cep) == 8:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            if response.status_code == 200:
                data = response.json()
                self.rua = data.get('logradouro', None)
                self.bairro = data.get('bairro', None)
                self.cidade = data.get('localidade', None)
                self.estado = data.get('uf', None)

@receiver(pre_save, sender=Pessoa)
def pre_save_pessoa(sender, instance, **kwargs):
    instance.pesquisar_cep()
