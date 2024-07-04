from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from cadastro.choices import *
import requests
import re
from datetime import date

class Lideranca(models.Model):
    nome = models.CharField(max_length=100)
    bairro_de_atuacao = models.CharField(max_length=100, choices=BAIRROS_SAO_GONCALO)
    telefone_whatsapp = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    tipo_de_atuacao = models.CharField(max_length=100)
    acordo = models.FileField(upload_to='acordos/', blank=True, null=True)
    foto = models.ImageField(upload_to='liderancas/', blank=True, null=True)

    def exibir_foto(self):
        if self.foto:
            return format_html('<img src="{}" width="50" height="50" />'.format(self.foto.url))
        return 'Sem foto'
    
    exibir_foto.short_description = 'Foto'

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField(blank=True, null=True, help_text = "Exemplo: 01/01/1990")
    genero = models.CharField(max_length=10, choices=SEXO_CHOICES)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    rua = models.CharField(max_length=255, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=10, default='000')
    idade = models.IntegerField(blank=True, null=True)
    titulo_eleitor = models.CharField(max_length=20, blank=True, null=True, unique=True)
    zona_eleitoral = models.CharField(max_length=10, blank=True, null=True)
    secao_eleitoral = models.CharField(max_length=10, blank=True, null=True)
    local_de_votacao = models.CharField(max_length=100, blank=True, null=True)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    nao_consta = models.BooleanField(default=False)
    apto_a_votar = models.BooleanField(default=False)
    votante = models.BooleanField(default=False)
    filhos = models.BooleanField(default=False)
    grau_de_influencia = models.CharField(max_length=10, choices=[('baixo', 'Baixo'), ('medio', 'Médio'), ('alto', 'Alto'), ('nenhum', 'Nenhum')])
    lideranca = models.ForeignKey(Lideranca, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    observacao = models.TextField(blank=True, null=True, verbose_name="Histórico")

    def whatsapp_link(self):
        if self.whatsapp:
            return f'https://api.whatsapp.com/send?phone={self.whatsapp}'
        return ''

    def save(self, *args, **kwargs):
        self.calcular_idade()
        self.verificar_votante()
        self.pesquisar_cep()
        super(Pessoa, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.lideranca.nome}" if self.lideranca else self.nome
    
    class Meta:
        permissions = [
            ("can_view_own_pessoa", "Can view own pessoa"),
        ]

    def calcular_idade(self):
        if self.data_de_nascimento:
            today = date.today()
            return today.year - self.data_de_nascimento.year - (
                (today.month, today.day) < (self.data_de_nascimento.month, self.data_de_nascimento.day)
            )
        return None
    
    def clean(self):
        super().clean()
        if self.data_de_nascimento:
            try:
                # Tenta converter a data para um formato válido
                if isinstance(self.data_de_nascimento, str):
                    self.data_de_nascimento = datetime.strptime(self.data_de_nascimento, '%DD/%MM/%YYYY').date()
            except ValueError:
                raise ValidationError('Formato de data inválido. Use DDMMYYYY.')

    calcular_idade.short_description = 'Idade'

    def verificar_votante(self):
        if self.idade and self.idade >= 16:
            self.votante = True
        else:
            self.votante = False

    def pesquisar_cep(self):
        cep = re.sub(r'\D', '', self.cep)
        if len(cep) == 8:
            try:
                response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
                if response.status_code == 200:
                    data = response.json()
                    self.rua = data.get('logradouro', '')
                    self.bairro = data.get('bairro', '')
                    self.cidade = data.get('localidade', '')
                    self.estado = data.get('uf', '')
            except requests.RequestException:
                pass
