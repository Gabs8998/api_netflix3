from django.shortcuts import render
from .models import Filmes, Genero
from .serializer import FilmesSerializers, GeneroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def listar_filmes(request):
    if request.method == 'GET':
        queryset = Filmes.objects.all()
        serializer =FilmesSerializers(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FilmesSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            

class FilmesViews(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializers

class FilmesDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializers

class GeneroViews(RetrieveUpdateDestroyAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    

    