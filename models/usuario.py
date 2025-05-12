from app import db
from flask_login import UserMixin

class Usuario(db.model, UserMixin):
    __tablename__ = 'usuarios'
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(20))
    email = Column(db.String(100))
    senha = Column(db.String(100))

    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = senha