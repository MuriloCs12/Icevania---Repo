from flask import render_template, request, redirect, flash, Blueprint
from models.usuario import Usuario
from utils import db, lm
from flask_login import login_user, logout_user, login_required
import hashlib

bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

@lm.user_loader
def load_user(id):
	usuario = Usuario.query.filter_by(id = id).first()
	return usuario

@bp_usuarios.route('/usuario', methods=['POST'])
def create_usuario():
    username = request.form.get('username')
    email = request.form.get('email')
    senha = request.form.get('senha')
    senha_hash = hashlib.sha256(senha.encode())
    csenha = request.form.get('csenha')
    
    if senha == csenha:
        usuario = Usuario(username, email, senha_hash.hexdigest())
        db.session.add(usuario)
        db.session.commit()
        flash ('Dados cadastrados com sucesso')
        return redirect('/entrar')
    else:
        flash ('Erro. Senhas não correspondentes')
        return redirect('/registrar')