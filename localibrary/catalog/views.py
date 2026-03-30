from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre, Language
from django.views.generic import ListView, DetailView


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_fantasy_books = Genre.objects.filter(name__icontains='fantasy').count()

    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_fantasy_books' : num_fantasy_books, 
        'num_visits': num_visits,
        }

    return render(request, 'index.html', context=context)

class BookListView(ListView):
    model = Book 
    context_object_name = 'book_list'
    #queryset = Book.objects.filter(title__icontains='war')
    paginate_by = 1
    
class BookDetailView(DetailView):
    model = Book
    
class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
    paginate_by = 3
    
class AuthorDetailView(DetailView):
    model = Author

class LanguageListView(ListView):
    model = Language
    context_object_name = 'language_list'
    #template_name = 'catalog/languages_list.html'

class BookInstanceListView(ListView):
    model = BookInstance
    context_object_name = 'bookinstance_list'
    paginate_by = 10


class BookInstanceDetailView(DetailView):
    model = BookInstance
    context_object_name = 'bookinstance'
