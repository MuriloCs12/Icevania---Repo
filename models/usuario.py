from utils import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = senha  