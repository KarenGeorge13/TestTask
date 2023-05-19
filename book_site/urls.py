from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path(r'registr/', views.RegistrView.as_view(), name='registr'),
    path(r'', views.BookListView.as_view(), name='books'),
    path(r'books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path(r'add_book/', views.BookAddView.as_view(), name='add_book'),
    path(r'update_book/<int:pk>/', views.BookUpdateView.as_view(), name='update_book'),
    path(r'book_delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),

    path(r'authors/', views.AuthorListView.as_view(), name='authors'),
    path(r'genres/', views.BookGenreListView.as_view(), name='genres'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

