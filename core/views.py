from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.shortcuts import render

from .models import Characters,Books
from .serializers import CharactersSerializer, BooksSerializer


def index(request):
    return render(request, 'index.html')

#View Livros
class BooksAPIView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksAPIViewPutDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


#View Personagens
class CharactersAPIView(generics.ListCreateAPIView):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer


class CharactersAPIViewPutDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer