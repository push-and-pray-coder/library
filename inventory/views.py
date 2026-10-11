from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'inventory/book_list.html'
    context_object_name = 'books_list'

class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'inventory/add_book.html'
    success_url = reverse_lazy('inventory_page')

class EditBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'inventory/edit_book.html'
    success_url = reverse_lazy('inventory_page')

class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy('inventory_page')
    template_name = 'inventory/delete_book.html'