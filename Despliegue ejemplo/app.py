from flask import Flask, render_template

app = Flask(__name__)

# Página principal (registro)
@app.route('/')
def index():
    return render_template("index.html", titulo="Registro de cuenta")

# Página de inicio de sesión
@app.route('/login')
def login():
    return render_template("index2.html", titulo="Inicio de sesión")

if __name__ == '__main__':
    app.run(debug=True)





