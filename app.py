from flask import Flask, render_template, flash

app = Flask(__name__)

@app.route('/registrar')
def index():
    return render_template('pagina-registrar.html')

if __name__ == '__main__':
    app.run()