from rest_framework import serializers
from book_site.models import Book, Author, BookGenre
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False, queryset=Author.objects.all())
    genre = serializers.PrimaryKeyRelatedField(many=False, queryset=BookGenre.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'book_image', 'release_date', 'author', 'genre']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'full_name', 'author_image', 'birth_date']


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['username', 'password']
