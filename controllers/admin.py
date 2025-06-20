from flask import render_template, request, redirect, flash, Blueprint
from models.usuario import Usuario
from utils import db, lm
import sqlalchemy as sa
from urllib.parse import urlsplit
from flask_login import login_user, logout_user, login_required
import hashlib


bp_admin = Blueprint("admins", __name__, template_folder='templates')

@bp_admin.route('/admin', methods=['POST'])
def create_admin():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        senha_hash = hashlib.sha256(senha.encode())
        novo_admin = Usuario(username=nome, email=email, senha=senha_hash.hexdigest(), role="admin")
        db.session.add(novo_admin)
        db.session.commit()
        return redirect("/dashboard")