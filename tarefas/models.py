from django.db import models

# Create your models here.
class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    posicao = models.CharField(max_length=50)
    nascimento = models.CharField(max_length=20)
    cidade = models.CharField(max_length=80)
    foto = models.ImageField(upload_to='jogadores/')

    def __str__(self):
        return self.nome