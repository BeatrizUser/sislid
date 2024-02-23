from django.contrib.gis.db import models

class RegiaoAtuacao(models.Model):
    nome = models.CharField(max_length=100)
    bairros = models.ManyToManyField('Bairro', related_name='regioes_atuacao')

    def __str__(self):
        return self.nome

class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    coordenadas = models.PointField(null=True, blank=True)  # Campo para armazenar as coordenadas geográficas do bairro

    def __str__(self):
        return self.nome

class Lideranca(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=100)
    regiao_atuacao = models.ForeignKey(RegiaoAtuacao, on_delete=models.CASCADE)
    coordenadas = models.PointField(null=True, blank=True)  # Campo para armazenar as coordenadas geográficas da liderança

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    profissao = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=100)
    titulo_eleitor = models.CharField(max_length=20)
    lideranca = models.ForeignKey(Lideranca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
