from flask import Flask, request, jsonify, render_template


PEOPLE_FOLDER = 'static/photos'
CSS_FOLDER = 'static/css'
AUDIO_FOLDER = 'static/audio'

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config['UPLOAD_FOLDER2'] = CSS_FOLDER
app.config['UPLOAD_FOLDER3'] = AUDIO_FOLDER

# Create some test data for our catalog in the form of a list of dictionaries.
data  = [{
    "Antwort": "Erde",
    "Frage": "Welcher Planet ist das",
    "ID": 1,
    "Option1": "Merkur",
    "Option2": "Erde",
    "Option3": "Uranus"},
{
    "Antwort": "Erde",
    "Frage": "Welcher Planet ist das",
    "ID": 2,
    "Option1": "Merkur",
    "Option2": "Erde",
    "Option3": "Uranus"},
{
    "Antwort": "Erde",
    "Frage": "Welcher Planet ist das",
    "ID": 3,
    "Option1": "Merkur",
    "Option2": "Erde",
    "Option3": "Uranus"},
]

full_filename = 'static/photos/image.jpg'
stylesheet = 'static/css/button2.css'
audiodatei = 'static/audio/audio.mp3'


@app.route('/', methods=['GET'])
def home():
    if 'id' in request.args:
        id = int(request.args['id'])
        score = int(request.args['score'])
        return render_template('Richi.html', Frage=data[id]['Frage'], Antwort=data[id]['Antwort'],
                               Option1=data[id]['Option1'], Option2=data[id]['Option2'], Option3=data[id]['Option3'],
                               Bild='static\photos\image' + str(id) + '.jpg', score=score, durchgang=id, CSS=stylesheet,audio=audiodatei)
    else:
        return render_template('Richi.html', Frage=data[0]['Frage'], Antwort=data[0]['Antwort'] ,Option1=data[0]['Option1'], Option2=data[0]['Option2'],
                               Option3=data[0]['Option3'], Bild=full_filename, score=0, durchgang=0,CSS=stylesheet, audio=audiodatei)

@app.route('/api/v1/resources/fragen/all', methods=['GET'])
def api_all():
    return jsonify(data)


@app.route('/api/v1/resources/fragen', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for Zeile in data[:,1:]:
        if Zeile['ID'] == id:
            results.append(Zeile)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/v1/resources/write', methods=['POST'])
def write():
    if 'result' in request.args:
        print(bool(request.args['result']))

    else:
        return "Error: No id field provided. Please specify an id."


@app.route('/final', methods=['GET'])
def final():
    if 'score' in request.args:
        score = int(request.args['score'])
        return render_template('final.html', score=score,CSS=stylesheet,audio=audiodatei)

    else:
        return "Error: No score field provided. Please specify a score."

app.run(host='127.0.0.1', port=5000, debug=True)
