# Guia de Configuração

## Executando com Docker Compose

1. **Clonar o repositório**
```bash
    git clone git@github.com:GoodGD-Dev/twitter-clone.git
    cd twitterclone
```
3. **Construir e executar containers**
```bash
    docker-compose up --build
```
4. **Acessar a aplicação**
Acesse a aplicação em `http://localhost:8000`.

## Configurando `serverbackend` com Poetry

1. **Instalar dependências com Poetry**
```bash
    cd backend
    poetry install
```

2. **Executar migrações e migrations**
```bash
    poetry run python manage.py makemigrations
    poetry run python manage.py migrate
```

4. **Iniciar o servidor**
```bash
    poetry run python manage.py runserver
```

## Configurando o Frontend com npm

1. **Instalar dependências**
```bash
    cd ..
    cd frontend
    npm install
```

3. **Iniciar o servidor de desenvolvimento**
```bash
    npm start
```

5. **Acessar o frontend**
Acesse o frontend em `http://localhost:3000`

