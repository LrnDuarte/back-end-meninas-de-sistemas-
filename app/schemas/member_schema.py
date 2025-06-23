from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Inicialização da aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'  # ou use PostgreSQL, ex: 'postgresql://user:senha@host/db'

# Inicialização do banco e marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Modelo Member
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    role = db.Column(db.String(50))

    def __init__(self, name, email, phone, role):
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role

# Esquema de serialização com Marshmallow
class MemberSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Member
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    role = ma.auto_field()

# Instâncias do schema (para uso posterior)
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

# Criação das tabelas (executar uma vez)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
