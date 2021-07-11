from flask import Flask, Blueprint
from flask import render_template, request
import foo_api

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def search():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/')
def get_data():
    events = api.call(get_event, arg0, arg1)
    geocode = event['latitude'], event['longitude']
    return render_template('get_data.html', geocode = geocode)

if __name__ == '__main__':
    app.run()
