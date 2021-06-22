[![author](https://img.shields.io/badge/author-leovilani-green)](https://www.linkedin.com/in/leonardo-vilani-selan/) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/)

# Processo de ETL com Python e Airflow usando API do Spotify

## Sobre
Projeto de ETL(Extract, Transform e Load) utilizando Python com API do Spotify e Airflow para automatização. Com um token gerado pela própria plataforma do Spotify é possível fazer um *request* com os dados das músicas que você ouviu, pegando apenas as que eu ouvi nas ultimas 24 horas, montei um processo onde manualmente ou automaticamente com o Airflow esses dados são salvos em um banco de dados SQL.
O projeto foi proposto pela youtuber Inglesa [Karolina Sowinska](https://www.youtube.com/c/KarolinaSowinska) e tem como objetivo passar mesmo que de forma básica pelos processos de ETL.

## Tecnologias
As seguintes ferramentas foram usadas na construção do projeto:

- **Python**
- **Pandas**
- **SQLAlchemy**
- **Airflow**

## Extract
Com uma conta gratuita do Spotify, é possível gerar um token que dará acesso as musicas que você ouviu, vale notar que o token expira em algumas horas o ideal seria encontrar uma maneira de atualizar o token automaticamente.

## Transform
Depois de extrair os dados, eles são transformados em um arquivo JSON, onde eu posso escolher as informações que eu desejo e coloca-las em um dicionario python. Depois eu transformo esse dicionario em um DataFrame do pandas para facilitar a manipulação.

## Load
Utilizando o SQLAlchemy eu crio um banco de dados, esse banco de dados é então alimentado com os dados do DataFrame.

## Validação
Há algumas validações básicas, uma que indica se o DataFrame está vazio, outra indica se alguma chave primaria está repetida e uma que checa se existe valores nulos.

## Airflow
Construi apenas uma DAG simples para entender como funciona o Airflow, ela rodaria a cada dia de forma automática, executando o código de ETL.

## Sobre Mim
Recém-formado em Ciências da Computação, e apaixonado por Inteligência Artificial e dados, busco oportunidade para adquirir experiência com Data Science, Machine Learning, Data Engineer e Big Data.
* [LinkedIn](https://www.linkedin.com/in/leonardo-vilani-selan/)
