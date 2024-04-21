![image](https://github.com/estersassis/Trocalivro/assets/71738908/f3503cd7-a636-4b4a-ac35-43c8a153666a)

#### Membros:
- Ester Sara Assis Silva (Back-end, BD)
- Filipe Pirola Santos (Front-end, Design)
- Milena Corrêa Moreira (Front-end, Design)
- Lucas Santana do Carmo Sacramento (Back-end, BD)

#### Tecnologias
- Front-end: HTML, CSS, JavaScript
- Back-end: Python com framework Django
- Banco de Dados: SQLite

#### Objetivo do projeto e principais features

O sistema consiste em uma plataforma online de troca de livros, visando facilitar a comunicação entre leitores que gostariam de, ao mesmo tempo, desvincular-se de um livro e obter outro; Promovendo a rotatividade desses e evitando o prejuízo de seus compradores. 

Seu funcionamento principal será com base em uma plataforma onde o usuário poderá cadastrar livros os quais deseja e, utilizando a homepage ou a ferramenta de pesquisa, pode solicitar um livro de outro usuário. Ao receber essa solicitação, o usuário poderá visualizar os livros que o solicitante tem disponíveis e, se algum lhe interessar, confirmar a troca. Assim, os envolvidos poderão confirmar ou cancelar trocas pelo sistema e avaliar o processo, de forma a atribuir uma reputação aos usuários, conferindo confiabilidade ao sistema. 

### Backlog do Produto

1. Como usuário, gostaria de ver uma pagina principal com os livros mais recentes.
2. Como usuário, gostaria de me cadastrar e gerenciar meu cadastro na plataforma. 
3. Como usuário, gostaria de cadastrar e gerenciar o cadastro uma livro para troca. 
4. Como usuário, gostaria de pesquisar um livro.
5. Como usuário, gostaria de solicitar uma troca de livro com outro usuario.
6. Como usuário, gostaria de ver as solicitações de troca enviadas.
7. Como usuário, gostaria de ver as solicitações de troca recebidas.
8. Como usuário, gostaria de aceitar ou rejeitar uma troca de livro.
9. Como usuário, gostaria de cancelar uma troca.
10. Como usuário, gostaria de confirmar a finalização de uma troca.
11. Como usuário, gostaria de ver o status da minha troca.
12. Como usuário, gostaria de avaliar uma troca.
13. Como usuário, gostaria de ver o historico de trocas de livros.
14. Como usuário, gostaria de receber notificacao de uma possivel troca por email.
15. Como administrador, gostaria de excluir um usuário.
16. Como administrador, gostaria de excluir um livro.

### Backlog da Sprint

- História #1: Como usuário, gostaria de ver uma pagina principal com todos os livros.
    
    **Tarefas e responsáveis**:
    
    1. Criar setup Django [Ester]
    2. Criar entidades principais do projeto [Ester]
    3. Configurar banco de dados MySQL [Lucas]
    4. Criar design de tela inicial no figma [Milena]
    5. Criar tela inicial no frontend [Milena]
    6. Implementar funcionalidade de ver os livros mais recentes na tela inicial no frontend [Milena]
    7. Implementar funcionalidade de listar livros no backend [Lucas]

- História #2: Como usuário, gostaria de me cadastrar e gerenciar meu cadastro na plataforma.
    
    **Tarefas e responsáveis**:
    
    1. Criar tela de cadastro no figma [Filipe]
    2. Criar tela de cadastro no frontend [Filipe]
    3. Implementar funcionalidade de criar usuário no backend [Ester]
    4. Implementar funcionalidade de deletar usuário no backend [Ester]
    5. Implementar funcionalidade de ler usuário no backend [Lucas]
    
- História #3: Como usuário, gostaria de cadastrar e gerenciar o cadastro uma livro para troca.
    
    **Tarefas e responsáveis**:
    
    1. Criar tela de cadastro de livro no figma [Filipe]
    2. Criar tela de cadastro de livro no frontend [Filipe]
    3. Implementar funcionalidade de cadastrar livro no backend [Lucas]
    4. Implementar funcionalidade de deletar livro cadastrado no backend [Lucas]
    5. Implementar funcionalidade de ver livro cadastrado no backend [Ester]

- História #4: Como usuário, gostaria de pesquisar um livro.
    
    **Tarefas e responsáveis**:
    
    1. Implementar funcionalidade de pesquisar livros no frontend [Milena]
    2. Implementar funcionalidade de listar livros coerentes com a pesquisa no backend [Lucas&Ester]

  ### Backlog da Sprint Revisado

- História #1: Como usuário, gostaria de ver uma pagina principal com todos os livros.
    
    **Tarefas e responsáveis**:
    
    1. Criar setup Django [Ester]
    2. Criar entidades principais do projeto [Ester]
    3. Configurar banco de dados SQLite [Lucas]
    4. Criar design de tela inicial no figma [Milena]
    5. Criar tela inicial no frontend [Milena]
    6. Implementar funcionalidade de ver os livros mais recentes na tela inicial no frontend [Milena]
    7. Implementar funcionalidade de listar livros no backend [Lucas]

    **Mudanças:** Não houveram.

- História #2: Como usuário, gostaria de me cadastrar e gerenciar meu cadastro na plataforma.
    
    **Tarefas e responsáveis**:
    
    1. Criar tela de cadastro no figma [Filipe]
    2. Criar tela de cadastro no frontend [Filipe]
    3. Implementar funcionalidade de criar usuário no backend [Ester]
    4. Implementar funcionalidade de editar usuário no backend [Ester]
    5. Implementar funcionalidade de ler usuário no backend [Lucas]

    **Mudanças:** Função de editar invés de excluir usuário.
    
- História #3: Como usuário, gostaria de cadastrar e gerenciar o cadastro uma livro para troca.
    
    **Tarefas e responsáveis**:
    
    1. Criar tela de cadastro de livro no figma [Filipe]
    2. Criar tela de cadastro de livro no frontend [Filipe]
    3. Implementar funcionalidade de cadastrar livro no backend [Lucas]
    4. Implementar funcionalidade de ver livro cadastrado no backend [Ester]

  **Mudanças:** Função de excluir livro excluído.

- História #4: Como usuário, gostaria de pesquisar um livro.
    
    **Tarefas e responsáveis**:
    
    1. Implementar funcionalidade de pesquisar livros no frontend [Milena]
    3. Implementar funcionalidade de listar livros coerentes com a pesquisa no backend [Lucas&Ester]

  **Mudanças:** Não houve.

- História #5: Como usuário, gostaria de solicitar uma troca de livro com outro usuario.

  **Tarefas e responsáveis**:
    
    1. Implementar funcionalidade de solicitar livros no frontend [Milena]
    2. Implementar funcionalidade de solicitar livros no backend [Lucas]

  **Mudanças:** História adicionada do backlog do produto.

 - História #6: Como usuário, gostaria de ver as solicitações de troca enviadas.

  **Tarefas e responsáveis**:
    1. Implementar funcionalidade de ver solicitação de livros enviadas no frontend [Milena]
    2. Implementar funcionalidade de ver solicitação de livros enviadas no backend [Lucas]

  **Mudanças:** História adicionada do backlog do produto.

 - História #7: Como usuário, gostaria de ver as solicitações de troca recebidas.

  **Tarefas e responsáveis**:
    1. Implementar funcionalidade de ver solicitação de livros recebidas no frontend [Milena]
    2. Implementar funcionalidade de ver solicitação de livros recebidas no backend [Lucas]

  **Mudanças:** História adicionada do backlog do produto.
 
  ### UMLs
![image](https://github.com/estersassis/Trocalivro/assets/71738908/1032dc6b-6880-4ace-8fdb-b10dede7f112)
![image](https://github.com/estersassis/Trocalivro/assets/71738908/7ba722c7-ef57-407c-8284-50847142b42b)

  ### Guia de Execução

    ```
    pip3 install -r requirements.txt # Baixar bibliotecas
    python trocalivro/manage.py makemigrations # Migrar banco
    python trocalivro/manage.py migrate # Migrar itens
    python trocalivro/manage.py runserver # Rodar server
    ```
