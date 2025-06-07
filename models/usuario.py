from utils import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String(255), nullable=True)

    def __init__(self, username, email, senha, image_path=None):
        self.username = username
        self.email = email
        self.senha = senha
        self.image_path = image_path