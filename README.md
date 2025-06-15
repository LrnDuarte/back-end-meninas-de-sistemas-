# 📦 Meninas SI - Backend API

API desenvolvida com **Flask** e **MySQL** para gerenciamento de:
- Administradores
- Membros
- Eventos
- Workshops
- Minicursos

Serialização feita com **Marshmallow**, arquitetura separada por camadas (controllers, services, models, schemas).

---

## 🚀 Tecnologias
- Python 3.13
- Flask
- SQLAlchemy
- Marshmallow
- MySQL

---

## 📁 Estrutura do Projeto

```
meninas_si-backend/
├── app/
│   ├── controllers/
│   │   ├── admin_controller.py
│   │   ├── event_controller.py
│   │   ├── member_controller.py
│   │   ├── short_course_controller.py
│   │   └── workshop_controller.py
│   │
│   ├── models/
│   │   ├── admin.py
│   │   ├── event.py
│   │   ├── member.py
│   │   ├── short_course.py
│   │   └── workshop.py
│   │
│   ├── routes/
│   │   ├── admin_routes.py
│   │   ├── event_routes.py
│   │   ├── member_routes.py
│   │   ├── short_course_routes.py
│   │   └── workshop_routes.py
│   │
│   ├── schemas/
│   │   ├── admin_schema.py
│   │   ├── event_schema.py
│   │   ├── member_schema.py
│   │   ├── short_course_schema.py
│   │   └── workshop_schema.py
│   │
│   ├── services/
│   │   ├── admin_service.py
│   │   ├── event_service.py
│   │   ├── member_service.py
│   │   ├── short_course_service.py
│   │   └── workshop_service.py
│   │
│   ├── __init__.py
│   ├── config.py
│   └── extensions.py
│
├── .env
├── requirements.txt
├── run.py
└── README.md
```

### 📄 Finalidade dos Arquivos

#### `app/`
Pasta principal da aplicação Flask.

- `controllers/`: define os métodos responsáveis pela inserção, retorno, atualização e exclusão dos dados de cada entidade.
- `models/`: contém os modelos do banco de dados com SQLAlchemy.
- `routes/`: define as rotas/endpoints responsáveis pela chamada dos métodos em `controllers/` de cada entidade.
- `schemas/`: serializadores e validadores com Marshmallow.
- `services/`: lógica de negócio, manipulação dos dados.
- `config.py`: configurações da aplicação.
- `extensions.py`: inicialização de extensões Flask (DB, Marshmallow, etc).
- `__init__.py`: inicialização da app Flask.

#### `.env`
Contém variáveis de ambiente, como dados de conexão com o banco de dados.

No arquivo ".env" altere o conteúdo das variáveis de ambiente de acordo com as credenciais da sua base de dados:
```python
DB_HOST=localhost
DB_PORT=3306 padrão do mysql ou outra porta que você definiu
DB_NAME=nome da base
DB_USER=usuário
DB_PASSWORD=senha

```

#### `requirements.txt`
Lista das bibliotecas necessárias para rodar o projeto.

#### `run.py`
Arquivo principal que executa o servidor Flask.

## 🔧 Instalação

```bash
# Clone o repositório
$ git clone https://github.com/Leandro-Coutinhodev/meninas_si-backend.git

# Acesse o diretório
$ cd meninas_si-backend

# Crie um ambiente virtual
$ python -m venv venv
$ source venv/bin/activate  # Linux/macOS
# ou
$ venv\Scripts\activate  # Windows

# Instale as dependências
$ pip install -r requirements.txt

# Execute a API
$ python run.py
```

## 📌 Endpoints principais
🔹 Admin

#### GET `/api/admin`

Retorna todos os administradores.

#### POST `/api/admin`

Cria um novo administrador.

Exemplo de JSON:
```json
{
  	"username": "@teste",
	"email": "teste@gmail.com",
	"password": "teste123",
	"created_time": "2025-06-12 00:00:00"
}
```
Fluxo interno:

    O JSON é recebido pelo controller via request.get_json().

    Os dados são validados e desserializados pelo AdminSchema com admin_schema.load(data).

    O objeto Admin é persistido no banco via SQLAlchemy.

    A resposta é retornada com admin_schema.jsonify(admin).

#### GET `/api/admin/<id_admin>`

Retorna os dados de um administrador específico.

#### PUT `/api/admin/<id_admin>`

Atualiza os dados de um administrador.

Exemplo de JSON:

Supondo que executamos o exemplo de json na rota POST /api/admin para criar um novo administrador, e que esse seja o primeiro registro na base de dados, então receberá id_admin: 1 .
Vamos atualizar esse registro executando o seguinte endpoint:

#### PUT `/api/admin/1`

```json
{
  	"username": "@teste",
	"email": "teste@gmail.com",
	"password": "teste@teste",
	"created_time": "2025-06-12 00:00:00"
}
```
Ao executar atualizamos o campo "password" de "teste123" para "teste@teste"

#### DELETE `/api/admin/<id_admin>`

Remove o administrador.
