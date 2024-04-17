from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from library.models import Book, Profile


def index(request):
    num_books = Book.objects.all().count()
    book_list = Book.objects.all()

    context = {
        'num_books': num_books,
        'book_list': book_list
    }

    return render(request, 'index.html', context=context)

@login_required
def profile(request):
    return render(request, 'profile.html')

def book_detail_view(request, id):
    book = Book.objects.get(id=id)

    return render(request, 'book_detail.html', context={'book': book})