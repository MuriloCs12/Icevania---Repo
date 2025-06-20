from flask import Flask, render_template, flash, abort, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
from controllers.usuario import bp_usuarios
from controllers.admin import bp_admin
from utils import db, lm
from roles import role_required
from models.usuario import Usuario

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.config['SECRET_KEY'] = 'abuble'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix = '/usuarios')
app.register_blueprint(bp_admin, url_prefix = '/admin')
migrate = Migrate(app, db)


db.init_app(app)
lm.init_app(app)

@app.route('/registrar')
def registrar():
    return render_template('pagina-registrar.html')

@app.route('/')
def login():
    return render_template('pagina-login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    return render_template('futuro-dashboard.html')

@app.route("/admin/criar", methods=["GET", "POST"])
@role_required("superadmin")
def criar_admin():
    return render_template("form_criar_admin.html")

@app.route("/admin/lista")
@role_required("superadmin")
def listar_admins():
    admins = Usuario.query.filter(Usuario.role == "admin").all()
    return render_template("lista_admins.html", admins=admins)

@app.route("/admin/promover/<int:user_id>")
@role_required("superadmin")
def promover_para_superadmin(user_id):
    user = Usuario.query.get(user_id)
    if user and user.role == "admin":
        user.role = "superadmin"
        db.session.commit()
        return "Promovido com sucesso!"
    abort(404)


if __name__ == '__main__':
    app.run()