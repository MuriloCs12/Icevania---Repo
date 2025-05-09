from flask import Flask, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pagina-base-entrar.html')

if __name__ == '__main__':
    app.run()