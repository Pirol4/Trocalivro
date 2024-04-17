from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from library.models import Book, User


def index(request):
    num_books = Book.objects.all().count()
    book_list = Book.objects.all()

    context = {
        'num_books': num_books,
        'book_list': book_list
    }

    return render(request, 'index.html', context=context)

def book_detail_view(request, id):
    book = Book.objects.get(id=id)
    
    return render(request, 'book_detail.html', context={'book': book})