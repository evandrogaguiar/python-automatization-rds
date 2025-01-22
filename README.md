# Finalizar Querys Lentas - MySQL

Este repositório contém uma automatização em Python que conecta em um RDS MySQL e busca por querys
que estejam sendo executadas por um longo período, ou de acordo com os critérios determinados pelo usuário.

## Requirements

[![My Skills](https://skillicons.dev/icons?i=python&perline=1)](https://skillicons.dev)  [Python](https://www.python.org/downloads/)

### Como Executar

**Instalar as dependências**

```bash
pip install -r requirements.txt
```

**Rodar a aplicação**

```bash
python main.py
```

As credenciais de conexão com o banco, são determinadas no arquivo * `.env`

```bash
cp .env.example .env
```