from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from library.forms import SignUpForm
from library.models import Book, Profile


def index(request):
    num_books = Book.objects.all().count()
    book_list = Book.objects.all()

    context = {
        'num_books': num_books,
        'book_list': book_list
    }

    return render(request, 'index.html', context=context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.instance
            user.save()
            user.refresh_from_db()
            user.profile.firstname=form.cleaned_data.get('firstname')
            user.profile.lastname=form.cleaned_data.get('lastname')
            user.profile.email=form.cleaned_data.get('email')
            user.profile.phone_number=form.cleaned_data.get('phone_number')
            user.profile.address=form.cleaned_data.get('address')    
            user.password = form.cleaned_data.get('password1')
            user.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    # Adicionar aqui listagem de livros da pessoa [Lucas]
    return render(request, 'profile.html')

@login_required
def book_add(request):
    # Adicionar aqui adição de livro [Lucas]
    return render(request, 'book_add.html')

def book_detail_view(request, id):
    book = Book.objects.get(id=id)

    return render(request, 'book_detail.html', context={'book': book})
