from rest_framework import permissions, generics
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.http import HttpResponseRedirect

from book_site.serializers import BookSerializer, BookGenreSerializer, AuthorSerializer, \
    UserSerializer, SearchSerializer, SortSerializer
from book_site.models import Book, Author, BookGenre


class RegistrView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permissions = [permissions.IsAuthenticated]


class BookGenreListView(generics.ListCreateAPIView):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    permissions = [permissions.IsAuthenticated]


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]
    sort_order = ('release_date', '-release_date')

    def get_queryset(self):
        author = self.request.query_params.get('author')
        genre = self.request.query_params.get('genre')
        if author and genre:
            queryset = self.queryset.filter(author__full_name__contains=author)
            queryset = queryset.filter(genre__name__contains=genre)
            return queryset
        if author:
            queryset = self.queryset.filter(author__full_name__contains=author)
            return queryset
        if genre:
            queryset = self.queryset.filter(genre__name__contains=genre)
            return queryset
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        sort = self.request.query_params.get('ascending')
        if sort:
            cur_sort_order = 0
        else:
            cur_sort_order = 1
        books_list = self.get_queryset().order_by(self.sort_order[cur_sort_order])
        return Response(
            {'user': request.user, 'books_list': books_list, 'search': SearchSerializer(), 'sort': SortSerializer},
            template_name=r'book_site\books.html'
        )

    def delete(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class BookAddView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [permissions.IsAuthenticated]


class BookUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [permissions.IsAuthenticated]


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        book = BookSerializer(self.get_object())
        author = AuthorSerializer(self.get_object().author)
        genre = BookGenreSerializer(self.get_object().genre)
        return Response({'user': request.user, 'book': book, 'author': author, 'genre': genre}, template_name=r'book_site\book_detail.html')


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return HttpResponseRedirect('/books/')














