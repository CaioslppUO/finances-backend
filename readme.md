# Plataforma de Controle de Despesas Mensais — Back-end

## Descrição

Este repositório contém o **back-end** do projeto desenvolvido como **Trabalho de Conclusão de Curso (TCC)** da pós-graduação em Desenvolvimento Fullstack, pela PucRS.  
O sistema consiste em uma **plataforma para controle de despesas mensais**, permitindo o registro, organização e visualização de gastos por período, categorias e usuários.

O back-end é responsável por:

-   Expor uma **API RESTful** para consumo pelo front-end
-   Gerenciar autenticação e autorização de usuários
-   Aplicar regras de negócio relacionadas ao controle financeiro
-   Persistir os dados em um banco de dados **PostgreSQL**

A aplicação foi desenvolvida utilizando **Python**, **Django** e **Django REST Framework**, seguindo boas práticas de organização de código, separação de responsabilidades e preparação para ambientes de desenvolvimento e produção.

---

## Sumário

-   [Tecnologias Utilizadas](#-tecnologias-utilizadas)
-   [Instalação](#-instalação-ubuntu)
    -   [Dependências](#dependências)
    -   [Configuração do Ambiente](#configuração-do-ambiente)
    -   [Docker e Docker Compose](#docker-e-docker-compose)
-   [Execução](#execução)
    -   [Desenvolvimento](#desenvolvimento)
    -   [Produção](#produção)
-   [Considerações Finais](#considerações-finais)

---

## Tecnologias Utilizadas

-   Python 3
-   Django
-   Django REST Framework
-   PostgreSQL
-   Docker
-   Docker Compose

---

## Instalação

### Dependências

```bash
sudo apt update && sudo apt install python3 python3-pip python3-virtualenv git
```

### Configuração do Ambiente

1. Clonar o repositório

```bash
git clone https://github.com/CaioslppUO/finances-backend
```

2. Criar o ambiente virtual

```bash
cd finances-backend
python3 -m virtualenv venv
```

3. Instalar as dependências

```bash
source venv/bin/activate
python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
```

4. Criar arquivo .env na raiz do projeto e preencher os valores corretos.

```bash
DEBUG=
SECRET_KEY=

DB_ENGINE=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

ALLOWED_HOSTS=
```

### Docker e Docker Compose

1. Limpar o ambiente.

```bash
sudo apt remove docker docker-engine docker.io containerd runc
```

2. Instalar dependências.

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
```

3. Adicionar e configurar chaves.

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

4. Instalar docker e docker compose.

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

5. Adicionar usuário ao grupo do docker.

```bash
sudo usermod -aG docker $USER
```

## Execução

### Desenvolvimento

1. Ativar o virtualenv.

```bash
souce venv/bin/activate
```

2.  Executar.

Criar as migrações do banco.

```bash
python3 manage.py makemigrations
```

Executar migrações.

```bash
python3 manage.py migrate
```

Criar super usuário.

```bash
python3 manage.py createsuperuser
```

Rodar o servidor.

```bash
python3 manage.py runserver
```

### Produção

1. Executar o container docker.

```bash
docker compose up -d
```

## Considerações Finais

Este projeto foi desenvolvido com fins acadêmicos, como parte do Trabalho de Conclusão de Curso (TCC) da pós-graduação, aplicando conceitos de arquitetura de software, desenvolvimento de APIs REST, conteinerização e boas práticas no desenvolvimento back-end com Django.

Autor: Caio Cezar das Neves Moreira
