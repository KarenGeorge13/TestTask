from django.contrib import admin
from book_site.models import Book, Author, BookGenre

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookGenre)