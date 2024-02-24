# models.py

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import requests
import re

class Lideranca(models.Model):
    nome = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    contato = models.CharField(max_length=100, blank=True, null=True)
    # Outros campos específicos da liderança, se necessário

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    SEXO_CHOICES = (
        ('M', 'Mulher'),
        ('H', 'Homem'),
    )
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=255, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=50, blank=True)
    cep = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    idade = models.IntegerField(blank=True, null=True)
    titulo_eleitor = models.CharField(max_length=20)
    zona_eleitoral = models.CharField(max_length=10, blank=True, null=True)
    secao_eleitoral = models.CharField(max_length=10, blank=True, null=True)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    nao_consta = models.BooleanField(default=False)
    lideranca = models.ForeignKey(Lideranca, on_delete=models.CASCADE)

    # Método para realizar a pesquisa de CEP
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

    def __str__(self):
        return self.nome

# Chama o método pesquisar_cep antes de salvar uma instância de Pessoa
@receiver(pre_save, sender=Pessoa)
def pre_save_pessoa(sender, instance, **kwargs):
    instance.pesquisar_cep()
