from django.db import models
from typing import Any

class Filmes(models.Model):

    titulo = models.CharField (max_length=255)
    genero = models.CharField (max_length=255, blank=True,null=True )
    ano = models.CharField (max_length=255)
    idioma = models.CharField (max_length=255)
    classf = models.CharField (max_length=255)

    
class Genero(models.Model):
    genre = models.CharField(max_length=255)
