from rest_framework import permissions, renderers, generics
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from book_site.serializers import BookSerializer, BookGenreSerializer, AuthorSerializer, UserSerializer
from book_site.models import Book, Author, BookGenre


class RegistrView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [permissions.IsAuthenticated]
    # renderer_classes = [TemplateHTMLRenderer]

    # def get(self, request, *args, **kwargs):
    #     return Response({'books_list': self.queryset.all()}, template_name=r'book_site\books.html')


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        print(self.get_object().book_image)
        return Response({'book': self.get_object()}, template_name=r'book_site\book_detail.html')












