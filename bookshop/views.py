from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Book, Author
from django.urls import reverse_lazy

# Create your views here.
class Book_list_view(ListView):
    template_name = 'book_list.html'
    model = Book

class Book_detail_view(DetailView):
    template_name = 'book_detail.html'
    model = Book

class Book_create_view(CreateView):
    template_name = 'book_create.html'
    model = Book
    fields = ["title", "author", "publish_date", "isbn", "seller"]

class Book_update_view(UpdateView):
    template_name = 'book_update.html'
    model = Book
    fields = ["title", "author", "publish_date", "isbn", "seller"]

class Book_delete_view(DeleteView):
    template_name = 'book_delete.html'
    model = Book
    success_url = reverse_lazy('book_list')
