from django.shortcuts import render
from library.models import Book, User


def index(request):
    num_books = Book.objects.all().count()

    context = {
        'num_books': num_books
    }

    return render(request, 'index.html', context=context)