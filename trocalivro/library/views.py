from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from library.forms import SignUpForm, BookForm, EditProfile
from library.models import Book, Profile


# Criado função responsavel por exibir imagens dos livros
def display_book_image(book):
    image_path = '/library/static/'
    image_default_path = ''

    if book.image:
        if book.image.url.startswith(image_path):
            return book.image.url.replace(image_path, '')
    # se o livro nao tiver imagem associada, será exibida uma imagem padrão. A declarar
    return image_default_path


def index(request):
    num_books = Book.objects.all().count()
    book_list = Book.objects.all()

    # instanciado funcao para exibir a imagem dos livros
    for book in book_list:
       book.image_display_url = display_book_image(book) 

    context = {
        'num_books': num_books,
        'book_list': book_list
    }

    return render(request, 'index.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.firstname=form.cleaned_data.get('firstname')
            user.profile.lastname=form.cleaned_data.get('lastname')
            user.profile.email=form.cleaned_data.get('email')
            user.profile.phone_number=form.cleaned_data.get('phone_number')
            user.profile.address=form.cleaned_data.get('address')    
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    user_books = Book.objects.filter(owner=request.user.profile)

    for book in user_books:
        book.image_display_url = display_book_image(book)

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
    return render(request, 'profile.html')

@login_required
def send_books(request):
    return render(request, 'send_books.html')

@login_required
def received_books(request):
    return render(request, 'received_books.html')

def book_detail_view(request, id):
    book = Book.objects.get(id=id)

    # instanciado funcao para exibir a imagem dos livros
    book.image_display_url = display_book_image(book)

    return render(request, 'book_detail.html', context={'book': book})

def search_book(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
        for book in books:
            book.image_display_url = display_book_image(book) 
    else:
        books = []
    return render(request, 'index.html', {'book_list': books})
