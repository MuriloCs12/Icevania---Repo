from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user, logout_user, login_required, current_user
from flask_migrate import Migrate

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
migrate = Migrate(app, db)
lm = LoginManager(app)

db.init_app(app)
lm.init_app(app)

@app.route('/registrar')
def registrar():
    return render_template('pagina-registrar.html')

@app.route('/login')
def login():
    return render_template('pagina-login.html')



if __name__ == '__main__':
    app.run()