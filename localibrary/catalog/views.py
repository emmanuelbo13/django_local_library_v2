from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views.generic import ListView, DetailView


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_fantasy_books = Genre.objects.filter(name__icontains='fantasy').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_fantasy_books' : num_fantasy_books
        }

    return render(request, 'index.html', context=context)

class BookListView(ListView):
    model = Book 
    context_object_name = 'book_list'
    #queryset = Book.objects.filter(title__icontains='war')
    paginate_by = 1
    
class BookDetailView(DetailView):
    model = Book
    