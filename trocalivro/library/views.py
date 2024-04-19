from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from library.forms import SignUpForm, BookForm, EditProfile
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
            # retirado a linha de codigo `user=form.instance` que salvava o usuário antes de realizar o cadastro e atribuido o form.save() ao user
            user = form.save()
            # user.refresh_from_db()
            user.profile.firstname=form.cleaned_data.get('firstname')
            user.profile.lastname=form.cleaned_data.get('lastname')
            user.profile.email=form.cleaned_data.get('email')
            user.profile.phone_number=form.cleaned_data.get('phone_number')
            user.profile.address=form.cleaned_data.get('address')    
            # consertado problema da senha atribuindo o metodo set_password
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    # Adicionar aqui listagem de livros da pessoa [Lucas]
    user_books = Book.objects.filter(owner=request.user.profile)
    return render(request, 'profile.html', {'user_books': user_books})

@login_required
def edit_profile(request):
    # associando a sessão ao usuário.
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        # Atribuindo formulario a instancia do usuario
        form = EditProfile(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
        return redirect('users-profile')
    else:
        # independente se não for enviada
        form = EditProfile(instance=profile)

    # exibir na pagina de edição de perfil 
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def book_add(request):
    # Adicionar aqui adição de livro [Lucas]
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # Salvando as informações do formulario do livro e atribuindo ao usuário da sessão.
            book = form.save(commit=False)
            book.owner = request.user.profile
            book.save()
            # Assim que cadastrar o livro ir para a tela com as informações dele, ou ate mesmo voltar para a tela de perfil com os livros cadastrados.
            return redirect('book-detail', id=book.pk)
    else:
        form = BookForm()
    return render(request, 'book_add.html', {'form':form})

@login_required
def my_books(request):
    # Adicionar aqui adição de livro [Lucas]
    return render(request, 'profile.html')

# Colocar em cada pagina os livros que tem os status marcados  
@login_required
def send_books(request):
    return render(request, 'send_books.html')

@login_required
def received_books(request):
    return render(request, 'received_books.html')

def book_detail_view(request, id):
    book = Book.objects.get(id=id)

    return render(request, 'book_detail.html', context={'book': book})
