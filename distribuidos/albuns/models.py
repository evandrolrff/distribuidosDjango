from django.db import models
from django.utils import timezone


class Albuns(models.Model):
    nome = models.CharField(max_length=255)
    data_lancamento = models.DateField(blank=True, null=True)
    banda = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    album = models.ForeignKey('Albuns', models.SET_NULL, blank=True, null=True)
    nome = models.CharField(max_length=255)
    duracao = models.TimeField()

    def __str__(self):
        return self.nome