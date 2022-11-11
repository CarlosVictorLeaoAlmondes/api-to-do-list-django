Instalar as dependências do Django e do djangorestframework:

    pip install django djangorestframework

Criar o projeto:

    django-admin startproject nomeDoProjeto .

    O ponto no final é para instalar o projeto dentro do diretório atual

Entre na pasta do projeto para continuar executando os comandos

Instalar o app:

    django-admin startapp nomeDoApp

A partir desse momento, já é possível acessar o servidor do Django com o comando:

    python manage.py runserver

Caso acesse o servidor neste momento, provavelmente haverá "reclamações" no terminal, isso acontece pois por padrão, o Django tem algumas migrações do banco de dados para criar, para resolver isso, execute o seguinte comando no terminal:

    python manage.py migrate

    Esse comando irá criar as tabelas no banco de dados

Dentro da pasta do projeto haverá outra pasta de mesmo nome, então, no arquivo settings.py, adicione 'rest_framework' e 'nomeDoApp' dentro de INSTALLED_APPS = []

nomeDoApp/models.py é o arquivo que iremos utilizar para criar a tabela do toDo no banco de dados

Após criar os novos modelos, é preciso avisar para o banco de dados que temos modelo novo, com o seguinte comando no terminal:

    python manage.py makemigrations

    Com isso, são criadas as migrations do novo modelo

Agora para incluir essas migrations no banco de dados, utilize o seguinte comando:

    python manage.py migrate

Para finalizar, utilize o seguinte comando para ver se a API está funcionando, e acesse o servidor:

    python manage.py runserver
