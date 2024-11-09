# projetoFuzzy
## clonar repositório:
1. Digite o comando:
```bash   
git clone https://github.com/CopiniS/api_fuzzy.git
```

3. Criar uma pasta venvs dentro de api_fuzzy e digitar o comando dentro de /venvs:
```bash  
   python -m venv api_fuzzy
```
3. Ativar o ambiente virtual criado anteriormente com o comando:
```bash 
  api_fuzzy\Scripts\Activate
```
4. Com o ambiente virtual ativado, instalar o Django, a lib para utilizar o .env, e o driver do postgre:
```bash 
  pip install Django
```
```bash 
  pip install python-decouple
```
```bash 
  pip install psycopg2-binary
```

5. Instalar bibliotecas com o ambiente virtual ativado: 
```bash 
  pip install scikit-fuzzy
```
```bash 
  pip install djangorestframework
```
```bash 
  pip install numpy
```
```bash 
  pip install scipy
```
```bash 
  pip install packaging
```
```bash 
  pip install networkx
```
```bash 
  python -m pip install django-cors-headers
```

5. Criar um arquivo .env dentro da pasta /projeto/api_fuzzy:

   Adicionar nesse .env, os dados que estao no wpp

6. Criar um banco de dado postgre com o nome do banco, o usuario e a senha que estão no .env

7. Fazer as migrações pendentes:
```bash
python manage.py migrate
```

8. Rodar o servidor:
```bash
python manage.py runserver
```
