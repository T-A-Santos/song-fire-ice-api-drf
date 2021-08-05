from rest_framework import serializers

from .models import Books, Characters

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = (
            'id',
            'url',
            'name',
            'isbn',
            'authors',
            'numberOfPages',
            'publisher',
            'country',
            'mediaType',
            'released',
            'povCharacters',
            'cover',
            'linkToBuy',
            
        )

class CharactersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Characters
        fields = (
            'id',
            'url',
            'name',
            'gender',
            'culture',
            'born',
            'died',
            'titles',
            'aliases',
            'father',
            'mother',
            'spouse',
            'allegiances',
            'books',
            'povBooks',
            'tvSeries',
            'playedBy'
        )