from flask import Flask, render_template

# Configurando o Flask para servir a pasta 'static'
app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')  # A página index.html será servida quando a raiz for acessada

if __name__ == "__main__":
    app.run(debug=True)  # Rodando o servidor local em modo debug


