from rest_framework import serializers
from .models import Filmes, Genero

class FilmesSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Filmes
        fields = ['id', 'titulo', 'genre', 'ano', 'idioma', 'classf']

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'genre']