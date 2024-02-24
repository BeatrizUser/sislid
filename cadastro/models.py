# models.py

from django.db import models
from django.db.models.signals import pre_save
# models.py

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    idade = models.IntegerField(blank=True, null=True, max_length=2)
    titulo_eleitor = models.CharField(max_length=20)
    zona_eleitoral = models.CharField(max_length=10, blank=True, null=True)
    secao_eleitoral = models.CharField(max_length=10, blank=True, null=True)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    nao_consta = models.BooleanField(default=False)
    lideranca = models.ForeignKey(Lideranca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

@receiver(pre_save, sender=Pessoa)
def pre_save_pessoa(sender, instance, **kwargs):
    if instance.nao_consta:
        instance.nome_mae = 'N/A'
    elif not instance.nome_mae:  # Se o campo nome_mae estiver vazio
        instance.nome_mae = 'N/A'
