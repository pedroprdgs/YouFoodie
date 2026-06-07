# Guia do Usuário

## Pré-requisitos

- [Git](https://git-scm.com/install/)
  
- [Docker](https://www.docker.com/get-started/)
  
    > **Observação:** para utilização do docker em sistemas Windows é necessária utilização de WSL
  
- [Python](https://www.python.org/downloads/)

## Baixando o Projeto

```bash
git clone https://github.com/pedroprdgs/YouFoodie.git
cd YouFoodie
```

## Configurando o .env

```bash
touch .env
```

### Arquivo base

```env
MYSQL_HOST=mysql
MYSQL_PORT=3306
MYSQL_DATABASE=youfoodie
MYSQL_USER=cliente
MYSQL_PASSWORD=123456
SECRET_KEY=chave
```

Edite os valores conforme necessário.

## Instalando dependências

```bash
pip install -r requirements.txt
```

> [!WARNING]
> Caso o comando **pip** não seja suportado, você pode ter que configurar as variáveis de ambientes do seu sistema operacional
> e caso utilize algum sistema baseado em **Linux**, talvez seja necessário instalar algum pacote adicional para utilizaá-lo

## Subindo os Containers

```bash
docker compose up -d
```

## Acessando o Sistema

Abra:

```text
http://localhost:5000
```

ou

```text
http://127.0.0.1:5000
```

## Parando o Sistema

```bash
docker compose down
```
