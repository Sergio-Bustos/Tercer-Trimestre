from flask import Flask, render_template, request

app = Flask(__name__) # This line was missing

@app.route('/')
def index():
    return render_template("index.html", titulo="Desarrollo Web con Flask y Jinja2")

if __name__ == '__main__':
    app.run(debug=True)



