from flask import Flask, Blueprint
from flask import render_template, request
import requests

key = '47ec0d7d-ea0a-4a20-bcee-66b897ea33bb'

url = "https://geocode-maps.yandex.ru/1."

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

# @app.route('/')    
# def get_posts():
#     r = requests.get('https://api-maps.yandex.ru/2.1/?apikey=47ec0d7d-ea0a-4a20-bcee-66b897ea33bb API-ключ&lang=ru_RU')
#     data = r.text
#     jsonData = []
#     for post in data:
#         r = requests.get('https://api-maps.yandex.ru/2.1/?apikey=47ec0d7d-ea0a-4a20-bcee-66b897ea33bb API-ключ&lang=ru_RU')
#         r.text
#         jsonData.append(r.text)
#     jsonData = jsonify(jsonData)
#     print jsonData  
#     return jsonData

@app.route('/')
def get_data():
    events = api.call(get_event, arg0, arg1)
    geocode = event['latitude'], event['longitude']
    return render_template('get_data.html', geocode = geocode)

if __name__ == '__main__':
    app.run()
