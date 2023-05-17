from django.urls import path, include
from . import views



urlpatterns = [
    path(r'registr/', views.RegistrView.as_view(), name='registr'),
    path(r'books/', views.BookListView.as_view(), name='books'),
    path(r'books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]

