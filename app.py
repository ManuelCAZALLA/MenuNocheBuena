import os
from flask import Flask, render_template
import random

app = Flask(__name__)

from flask_cors import CORS
CORS(app)


# Lista de frases para la Nochebuena
frases = [
    "Abuelo te acuerdas cuando tirastes el porrón por el balcón porque estaba vacío.",
    "Abuela te acuerdas aquella vez que por mas que rezabas para llegar a casa sin cagarte, no hubo ayuda divina?.",
    "Abuelo es cierto que no te comiste el plato de sopa, porque no tenías cuchara?.",
    "Abuela te acuerdas cuando mandaste al abuelo a por un poco de huevo hilado? Compro 2 kilos.",
    "Abuela te acuerda cuando fuiste a los Villares y andastes mas que en el reto Araque?",
    "Os acordais la navidad tan buena que pasó el cura al llevarse el jamon de 200 euros"
    "Abuelo te acuerdas cuando tiraste al Paquito el Sigal porque no paraba de cantar y te tenias que ir a misa?"
    "Abuelo te acuerdas cuando tocaste las campanas a pino después de comer? Corria mas que Mbappe para la iglesia"
]

@app.route('/')
def home():
    frase_aleatoria = random.choice(frases)
    return render_template('index.html', frase = frase_aleatoria)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
