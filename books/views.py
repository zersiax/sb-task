from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book_list.html'
    login_url = 'login'
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class BookDetailView(LoginRequiredMixin, DetailView): 
    model = book
    template_name = 'book_detail.html'
    login_url = 'login'


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Book
    fields = ('title', 'author', 'rating')
    template_name = 'book_edit.html'
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    template_name = 'book_new.html'
    fields = ('title', 'rating', 'author',)
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


    def form_valid(self, form):
        return super().form_valid(self,form):
        form.instance.poster = self.request.user
