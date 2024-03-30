from django.template import loader
from django.http import HttpResponse
from .models import User, Book, Address
from django.shortcuts import render

def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def db_test(request):
    user = User.objects.all().values()
    template = loader.get_template('database_test.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))

# função responsável por exibir os livros na pagina books.html
def list_books(request):
    books = Book.objects.order_by('name')
    
    context = {'books': books}

    return render(request, 'books.html', context)