from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookDetailView(DetailView): 
    model = book
    template_name = 'book_detail.html'


class BookUpdateView(UpdateView): 
    model = Book
    fields = ('title', 'author', 'rating')
    template_name = 'book_edit.html'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_new.html'
    fields = ('title', 'rating', 'author', 'poster',)
    