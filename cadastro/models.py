from django.db import models

class Lideranca(models.Model):
    nome = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    contato = models.CharField(max_length=100, blank=True, null=True)
    # Outros campos específicos da liderança, se necessário

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10)
    idade = models.IntegerField()
    titulo_eleitor = models.CharField(max_length=20)
    zona_eleitoral = models.CharField(max_length=10)
    secao_eleitoral = models.CharField(max_length=10)
    nome_mae = models.CharField(max_length=100)
    lideranca = models.ForeignKey(Lideranca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome