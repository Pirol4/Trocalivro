from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from library.forms import SignUpForm, BookForm, EditProfile
from library.models import Book, Profile, BookExchange, StatusBook


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
   
    # Instanciado função para exibir a imagem dos livros
    for book in book_list:
       book.image_display_url = display_book_image(book) 

    book_list = list(reversed(book_list))

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

    user_books = list(reversed(user_books))

    return render(request, 'profile.html', {'user_books': user_books})


@login_required
def edit_profile(request):
    # Associando a sessão ao usuário.
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
            # Retirado função do front-end do usuario definir status do livro, todo livro cadastrado sera 'AVAILABLE'
            book.status = StatusBook.AVAILABLE.value
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
    # Instancia de todos os livros 
    book_exchanges = BookExchange.objects.all()
    
    user_books = []
    # Se o usuário que realizou a requisição for o usuário atual da sessão.
    for exchange in book_exchanges:
        if exchange.requester == request.user.profile:
            #incluir livros em uma lista de livros em troca.
            user_books.append(exchange.book)

    for book in user_books:
        book.image_display_url = display_book_image(book)

    user_books = list(reversed(user_books))

    # Exibir no front a lista que tem as solicitações de troca do usuário 
    return render(request, 'send_books.html', {'user_books': user_books})

@login_required
def received_books(request):

    # Recebe a instancia do banco de dados atrelado ao usuário na sessão
    book_exchanges = BookExchange.objects.filter(owner_id = request.user.profile)

    # Cria uma lista que será inclusa no contexto para exportar para o frontend
    user_books = []

    for exchange in book_exchanges:
        
        # Adiciona os livros associados a cada troca à lista de livros do usuário
        # Dicionario com o livro do usuário que foi requerido e o nome do usuário que solicitou. 
        book_info = {
            'book': exchange.book,
            'requester_name': exchange.requester.user.username,
        }
        user_books.append(book_info)
    
    
        
    # Para cada livro, atualiza a URL de exibição da imagem
    for book_info in user_books:
        book = book_info['book']
        book.image_display_url = display_book_image(book)

    user_books = list(reversed(user_books))
    
    return render(request, 'received_books.html', {'user_books': user_books})


def book_detail_view(request, id):
    # Retorna o livro
    book = Book.objects.get(id=id)

    # Instanciado funcao para exibir a imagem dos livros
    book.image_display_url = display_book_image(book)
    
    # Define a sessão do usuário none, isso se dá ao fato do usuário que não está autenticado não poder solicitar uma troca, é direcionado para login.
    user_profile = None
    # Se o usuário estiver autenticado, ai sim atribuir ao 'user_profile'
    if request.user.is_authenticated:
        user_profile = request.user.profile

    # Dicionario contendo o livro e o usuário, caso houver
    book_info = {
        'book' : book,
        'user' : user_profile
    }
    return render(request, 'book_detail.html', context={'book_info': book_info})

def search_book(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
        for book in books:
            book.image_display_url = display_book_image(book) 
    else:
        books = []
    return render(request, 'index.html', {'book_list': books})
    
# Função responsável por tratar as trocas entre os livros 
def request(request, id):

    if request.method == 'POST':
        # Verifica se o usuário está autenticado
        if not request.user.is_authenticated:
            # Redireciona o usuário para a página de login
            return redirect('login')  

        # Perfil do usuário que solicitou o livro
        requester_profile = request.user.profile

        # Livro que está sendo solicitado
        book = Book.objects.get(pk=id)

        # Verifica se o livro está disponível para troca
        if book.status != StatusBook.AVAILABLE.value:
            return redirect('index')  # Redireciona de volta para a página de detalhes do livro

        # Verifica se o usuário solicitando é o dono do livro se isso acontecer, Botão de solicitar livro não aparece.
        if book.owner == requester_profile:
            return redirect('index')

        # Cria uma instância de BookExchange para solicitar a troca
        BookExchange.objects.create(book=book, requester=requester_profile, owner=book.owner, status=StatusBook.IN_EXCHANGE.value)
        
        # Atualiza o status do livro para "IN EXCHANGE"
        book.status = StatusBook.IN_EXCHANGE.value
        book.save()

        # Quando o livro é solicitado com sucesso, o usuário é redirecionado para a pagina de solicitações enviadas.
        return redirect('send-books')  

    else:
        # Se o método da requisição não for POST, retornar para o index
        return redirect('index')
