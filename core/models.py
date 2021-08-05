from django.db import models

# Create your models here.
class Books(models.Model):
    
    url = models.URLField(unique=True, blank=True)
    name = models.CharField(max_length=255, blank=True, verbose_name='Nome')
    isbn = models.CharField(max_length=255, blank=True, verbose_name='ISBN')
    authors = models.CharField(max_length=255, blank=True, verbose_name='Autores')
    numberOfPages = models.SmallIntegerField(verbose_name='Numero de paginas')
    publisher = models.CharField(max_length=255, blank=True, verbose_name='Editora')
    country = models.CharField(max_length=255, blank=True, verbose_name='País')
    mediaType = models.CharField(max_length=255, blank=True,verbose_name='Tipo de Midia')
    released = models.DateTimeField(auto_now_add=False, verbose_name='Lançado')
    povCharacters = models.JSONField(default=dict, verbose_name='Personagens Principais')
    cover = models.TextField(blank=True, verbose_name='Capa')
    linkToBuy = models.URLField(blank=True, verbose_name='Link pra compra')

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.name + self.authors + self.publisher

    
class Characters(models.Model):

    url = models.URLField(unique=True, blank=True)
    name = models.CharField(max_length=255, blank=True, verbose_name='Nome')
    gender = models.CharField(max_length=8, verbose_name='Sexo')
    culture = models.CharField(max_length=255, blank=True, verbose_name='Cultura')
    born = models.CharField(max_length=255, blank=True, verbose_name='Nascido em')
    died = models.CharField(max_length=255, blank=True, verbose_name='Morto em')
    titles = models.JSONField(default=dict, verbose_name='Títulos')
    aliases = models.JSONField(default=dict, verbose_name='Apelidos')
    father = models.CharField(max_length=255, blank=True, verbose_name='Pai')
    mother = models.CharField(max_length=255, blank=True, verbose_name='Mãe')
    spouse = models.CharField(max_length=255, blank=True, verbose_name='Conjuge')
    allegiances = models.JSONField(default=dict, verbose_name='Lealdades')
    books = models.JSONField(default=dict, verbose_name='Livros')
    povBooks = models.JSONField(default=dict, verbose_name='Livros Principais')
    tvSeries = models.JSONField(default=dict, verbose_name='Aparicoes na serie')
    playedBy = models.JSONField(default=dict, verbose_name='Ator')

    class Meta:
        verbose_name = 'Personagem'
        verbose_name_plural = 'Personagens'

    def __str__(self):
        return self.name + self.gender + self.culture + str(self.books)

