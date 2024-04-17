from django.template import loader
from django.http import HttpResponse
from .models import User, Book
from django.shortcuts import render
from users.forms import RegisterUserForm

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

def add_user(request):
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
    
    context = {
        'form': form
    }

    template = loader.get_template('register_user_template.html')
    return HttpResponse(template.render())