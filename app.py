from Flask import Flask, render_template, flash

app = Flask(__name__)

@routes.route('/')
def index():
    return

if __name__ == '__main__':
    app.run()