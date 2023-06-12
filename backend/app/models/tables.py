from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password =  password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

class Lote(db.Model):
    __tablename__ = "lotes"

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Integer)
    tamanho = db.Column(db.Integer)
    endereco = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, valor, tamanho, user_id):
        self.valor = valor
        self.tamanho = tamanho
        self.user_id = user_id
    
    def __repr__(self):
        return "<Lote %r>" % self.id
    
class Casa(db.Model):
    __tablename__ = "casas"
    
    id = db.Column(db.Integer, primary_key=True)
    tamanho = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lote_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    lote = db.relationship('User', foreign_keys=lote_id)