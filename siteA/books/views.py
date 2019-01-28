from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from books.models import Book, Author, Publisher

# Create your views here.
class BooksModelView(TemplateView):
    template_name = 'books/index.html'    
    
    def __init__(self):
        pass
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        print(context)
        return context
    
    
class BookList(ListView):    
    model = Book
    
class AuthorList(ListView):
    model = Author
    
class PublisherList(ListView):
    model = Publisher
    
class BookDetail(DetailView):    
    model = Book
    
class AuthorDetail(DetailView):
    model = Author
    
class PublisherDetail(DetailView):
    model = Publisher