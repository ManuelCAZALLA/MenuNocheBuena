from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de frases para la Nochebuena
frases = [
    "Abuelo te acuerdas cuando tirastes el porrón por el balcón porque estaba vacío.",
    "Abuela te acuerdas aquella vez que por mas que rezabas para llegar a casa sin cagarte, no hubo ayuda divina?.",
    "Disfruta de esta Nochebuena rodeado de tus seres queridos.",
    "Que la magia de la Navidad te ilumine siempre.",
    "¡Que tengas una maravillosa Nochebuena llena de amor!"
]

@app.route('/')
def home():
    # Seleccionar una frase aleatoria
    frase_aleatoria = random.choice(frases)
    return render_template('index.html', frase=frase_aleatoria)

if __name__ == "__main__":
    app.run(debug=True)
