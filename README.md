# Sistema de Gerenciamento de Usuários e Produtos
Este é um sistema de gerenciamento de usuários e produtos desenvolvido com o framework Django, baseado em conceitos de programação orientada a testes (TDD) e utilizando Generic Views.

## Funcionalidades
- Gerenciamento de usuários (criação, edição, listagem, listagem de um usuario)
- Gerenciamento de produtos (criação, edição, listagem, listagem de um produto)

## Iniciando o projeto

- Faça o clone do repositório em sua máquina local utilizando o comando: 
```git clone git@github.com:fjrjdev/Django-User-Prod-Manager.git```
-  Crie um ambiente virtual para o projeto. Isso é importante para garantir que as dependências do projeto não interfiram com outros projetos em sua máquina. Para criar o ambiente virtual, execute o comando 
```python -m venv nome_do_ambiente```
- Ative o ambiente virtual. Para fazer isso, execute o comando ```source nome_do_ambiente/bin/activate``` no Linux/MacOS ou ```nome_do_ambiente\Scripts\activate``` no Windows.
- Instale as dependências do projeto. 
- Com o ambiente virtual ativado, execute o comando ```pip install -r requirements.txt``` para instalar todas as dependências listadas no arquivo requirements.txt.
- Rode as migrações. Com as dependências instaladas, execute o comando ```python manage.py migrate``` para criar as tabelas necessárias no banco de dados.
- Inicie o servidor. Para iniciar o servidor, execute o comando ```python manage.py runserver``` e aguarde até que o servidor esteja pronto.
- Acesse a aplicação. Com o servidor iniciado, você pode acessar a aplicação digitando http://127.0.0.1:8000/ no seu navegador.

## Iniciando o projeto com Docker

<br>

- **Etapa 1: clonar o repositório**

```
git clone git@github.com:fjrjdev/Django-User-Prod-Manager.git
```

- **Etapa 2: Abra o diretório do repositório clonado**

```
cd Django-User-Prod-Manager
```

- **Etapa 3: Criar o aplicativo**

```
docker compose up --build
```
Esse comando criará as imagens e os contêineres necessários para o aplicativo.

- **Step 4: Start the application**

```
docker compose up
```

- **Etapa 5: Acessar o aplicativo**

```
Visite http://localhost:3000/ no seu navegador da Web.

Nota: Certifique-se de ter o docker em seu sistema antes de executar os comandos acima.
```

## Testes
Para executar os testes, utilize o comando ```python manage.py test.``` Isso irá executar todos os testes automatizados escritos para o projeto e exibir o resultado.

## Obs
Este é um exemplo básico de como o sistema funciona, portanto, pode haver necessidade de adaptações e melhorias para sua utilização em um ambiente de produção.
