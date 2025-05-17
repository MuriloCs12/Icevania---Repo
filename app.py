from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
from controllers.usuario import bp_usuarios
from utils import db, lm

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.config['SECRET_KEY'] = 'abuble'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix = '/usuarios')
migrate = Migrate(app, db)


db.init_app(app)
lm.init_app(app)

@app.route('/registrar')
def registrar():
    return render_template('pagina-registrar.html')

@app.route('/login')
def login():
    return render_template('pagina-login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('futuro-dashboard.html')


if __name__ == '__main__':
    app.run()