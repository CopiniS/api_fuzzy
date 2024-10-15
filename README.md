# projetoFuzzy
## clonar repositório:
1. Digite o comando:

  git clone https://github.com/CopiniS/api_fuzzy.git

2. Criar uma pasta venvs dentro de api_fuzzy e digitar o comando dentro de /venvs:

  python -m venv api_fuzzy

3. Ativar o ambiente virtual criado anteriormente com o comando:

  api_fuzzy\Scripts\Activate

4. Com o ambiente virtual ativado, instalar o Django, a lib para utilizar o .env, e o driver do postgre:

  pip install Django

  pip install python-decouple

  pip install psycopg2-binary

5. Criar um arquivo .env dentro da pasta /projeto/api_fuzzy:

   Adicionar nesse .env, os dados que estao no wpp

6. Criar um banco de dado postgre com o nome do banco, o usuario e a senha que estão no .env
