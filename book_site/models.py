from django.db import models
# Create your models here.


class Book(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    description = models.TextField(verbose_name='Описание')
    book_image = models.ImageField(verbose_name='Изображение книги', upload_to='images/', null=True, blank=True)
    release_date = models.DateField(verbose_name='Дата выпуска')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('BookGenre', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Author(models.Model):
    full_name = models.CharField(verbose_name='ФИО автора', max_length=150)
    author_image = models.ImageField(verbose_name='Изображение автора', upload_to='images/', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'



class BookGenre(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'



