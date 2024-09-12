from django.db import models
from typing import Any

class Genero(models.Model):
    genre = models.CharField(max_length=255)

class Filmes(models.Model):

    titulo = models.CharField (max_length=255)
    genre = models.ForeignKey (Genero, on_delete=models.CASCADE)
    ano = models.CharField (max_length=255)
    idioma = models.CharField (max_length=255)
    classf = models.CharField (max_length=255)
    