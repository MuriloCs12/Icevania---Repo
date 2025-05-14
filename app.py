from flask import Flask, render_template, flash

app = Flask(__name__)

@app.route('/registrar')
def registrar():
    return render_template('pagina-registrar.html')

@app.route('/login')
def login():
    return render_template('pagina-login.html')



if __name__ == '__main__':
    app.run()