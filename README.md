# Django Attractions API
Projeto de uma Web API de pontos turísticos, onde o seu desenvolvimento tem como objetivo o estudo das seguintes tecnologias:

- Python
- Django
- Django REST Framework


# Requisitos
- Python


# Como executar?
### Passo 1
Abra o terminal na raiz desse projeto e crie o seu ambiente virtual Python utilizando o comando `python -m venv venv`

### Passo 2
- Ative o seu ambiente virtual `. venv/bin/activate`

### Passo 3
- Instale o Django `pip install django`

### Passo 4
- Instale o Django REST framework `pip install djangorestframework`

### Passo 5
- Faça uma sincronização do banco de dados `python manage.py migrate`

### Passo 6
- Crie o seu superusuário para acessar a área administrativa executando o comando `python manage.py createsuperuser` e fornecendo um nome de usuário, e-mail e senha

### Passo 7
- Inicie o servidor utilizando o comando `python manage.py runserver`

### Passo 8
- Abra o seu navegador e acesse a url `http://127.0.0.1:8000` ou a parte administrativa com `http://127.0.0.1:8000/admin/`


# Licença
Esse projeto está licenciado sob a licença MIT License. Veja o arquivo [LICENSE](https://github.com/isnardsilva/django-attractions-api/blob/master/LICENSE) para ter mais informações.
