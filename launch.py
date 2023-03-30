from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def index():
    note = ''
    results=[]
    if request.method == 'POST':
        depots_du_gouvernement= request.form['depots_du_gouvernement']
        reserves= request.form['reserves']
        engagementsexterieursamoyensetlongstermes= request.form['engagementsexterieursamoyensetlongstermes']
        avoirs_exterieurs= request.form['avoirs_exterieurs']
        depots_a_vue= request.form['depots_a_vue']


        model = joblib.load('model/model.pkl')
        data = [[depots_du_gouvernement,reserves,engagementsexterieursamoyensetlongstermes,avoirs_exterieurs,depots_a_vue]]
        results = [depots_du_gouvernement,reserves,engagementsexterieursamoyensetlongstermes,avoirs_exterieurs,depots_a_vue]
        val = np.array(data, dtype=float)
        predict =  model.predict(val)
        note = giveNote(predict)

        print(note)

    # affichage de la page
    return render_template('index.html', note=note, results=results)


def giveNote(note):
    if note[0] == 0:
        return "B"
    elif note[0] == 1:
        return "C"
    elif note[0] == 2:
        return "A"
    else:
        return "None"


if __name__ == "__main__":
    app.run(debug=True)
