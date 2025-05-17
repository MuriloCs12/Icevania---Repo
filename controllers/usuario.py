from flask import render_template, request, redirect, flash, Blueprint
from models.usuario import Usuario
from utils import db, lm
import sqlalchemy as sa
from urllib.parse import urlsplit
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
    
    username_existente = Usuario.query.filter_by(username=username).first()
    if username_existente:
        flash('Nome de usuário já está em uso')
        return redirect('/registrar')
    
    if senha == csenha:
        usuario = Usuario(username, email, senha_hash.hexdigest())
        db.session.add(usuario)
        db.session.commit()
        flash ('Dados cadastrados com sucesso')
        return redirect('/entrar')
    else:
        flash ('Erro. Senhas não correspondentes')
        return redirect('/registrar')

@bp_usuarios.route('/auth_usuario', methods=['POST'])
def autenticar_usuario():
    login = request.form.get('login')
    senha = request.form.get('senha')

    user = Usuario.query.filter((Usuario.username == login) | (Usuario.email == login)).first()

    if user and user.senha == hashlib.sha256(senha.encode()).hexdigest():
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = ('/dashboard')
        return redirect(next_page)
    
  
    flash('Usuário ou senha inválidos.', 'danger')
    return redirect('/entrar')