Clone o repositório:

- git clone https://github.com/leluizedson/ecommerce_nadic.git
- cd ecommerce_nadic

Crie e ative um ambiente virtual:

- python -m venv .venv
# Linux / macOS
- source .venv/bin/activate
# Windows
- .venv\Scripts\activate

Instale as dependências:
- pip install -r requirements.txt
  
Migrações e registrar administrador
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

  Iniciar o servidor de desenvolvimento:
  - python manage.py runserver
 
  Acesse: http://127.0.0.1:8000/
