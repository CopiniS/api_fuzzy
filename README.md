# projetoFuzzy
## Executar a Api:
1. Digite o comando:
```bash   
git clone https://github.com/CopiniS/api_fuzzy.git
```

3. Criar uma pasta venvs dentro de /backend e digitar o comando dentro de /venvs:
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

   Adicionar nesse .env, os dados:

```bash 
SECRET_KEY=django-insecure-1#5#^@4cw3)890)nc78q#8xz40ftj1%kk(go0n1(3fmlsr)(9w
DB_NAME = api_fuzzy
DB_USER = postgres
DB_PASSWORD = admin
DB_HOST = localhost
DB_PORT = 5432
```

*O BANCO DE DADOS SERÁ USADO APENAS NO PROJETO DE PESQUISA
NÃO A NECESSIDADE DESSAS PRÓXIMAS LINHAS PARA TESTAR A API POR ENQUANTO*

6. Criar um banco de dado postgre com o nome do banco, o usuario e a senha que estão no .env

7. Fazer as migrações pendentes:
```bash
python manage.py migrate
```

8. Rodar o servidor:
```bash
python manage.py runserver
```

## Rotas da Api:

1. Macieiras:
   1. Pré-plantio:
      PATH: http://localhost:8000/macieiras/pre-plantio/
      METHOD: POST
      LAYOUT BODY: {
                  	"ph_agua" : "5.78",
                  	"fosforo": "9.6",
                  	"potassio": "117",
                  	"calcio": "1",
                  	"magnesio": "1.19",
                  	"indice_smp": "5",
                  	"ctc": "19.52",
                  	"argila": "35",
                  	"areaPlantada": "10"
                  }

2. Consorciação de gramíneas e leguminosas de estação fria:
   1. Pré-plantio:
      PATH: http://localhost:8000/gramineas-leguminosas-frias/pre-plantio/
      METHOD: POST
      LAYOUT BODY: {
                  	"ph_agua" : "5.78",
                  	"fosforo": "9.6",
                  	"potassio": "117",
                  	"calcio": "1",
                  	"magnesio": "1.19",
                  	"indice_smp": "5",
                  	"ctc": "19.52",
                  	"argila": "35",
                  	"areaPlantada": "10"
                  }
      

   





   
