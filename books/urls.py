from django.urls import path

from .views import (
    BookListView,
    BookUpdateView,
    BookDetailView,
    BookDeleteView,
    BookCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         BookUpdateView.as_view(), name='book_edit'), 
    path('<int:pk>/',
         BookDetailView.as_view(), name='book_detail'), 
    path('<int:pk>/delete/',
         BookDeleteView.as_view(), name='book_delete'), 
    path('new/', BookCreateView.as_view(), name='book_new'),
    path('', BookListView.as_view(), name='book_list'),
]