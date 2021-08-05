from django.urls import path
from .views import (BooksAPIView,
                    CharactersAPIView,
                    BooksAPIViewPutDelete,
                    CharactersAPIViewPutDelete,
                    index,
                    )


urlpatterns = [
    path('', index, name='Index'),
    path('books/', BooksAPIView.as_view(), name='Livros'),
    path('characters/', CharactersAPIView.as_view(), name='Personagens'),
    path('books/<int:pk>/', BooksAPIViewPutDelete.as_view(), name='Livros_edit_delete'),
    path('characters/<int:pk>/', CharactersAPIViewPutDelete.as_view(), name='Personagens_edit_delete'),
]
