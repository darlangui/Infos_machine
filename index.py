from flask import Flask, render_template, request, jsonify
import json
import requests



app = Flask(__name__)

def search_ip(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    return json.loads(response.text)

def info(result):
    print(f"Pais :", {result['country']})
    print(f"Estado :", {result['regionName']})
    print(f"Cidade :", {result['city']})
    print(f"Latitude :", {result['lat']})
    print(f"Longitude :", {result['lon']})
    print(f"Zip :", {result['zip']})
    print(f"ISP :", {result['isp']})
    print(f"Organização :", {result['org']})

@app.route('/get_resolution', methods=['POST'])
def get_resolution_data():
    width = request.form.get('width')
    height = request.form.get('height')
    resolution = {'width': width, 'height': height}
    print(f"Screen Resolution: {width} x {height}")
    return "OK"

@app.route('/get_resolution')
def get_resolution():
    return render_template('index.html')

@app.route('/')
def index():  # put application's code here
    '''info(search_ip(request.remote_addr))'''
    print('\n\n------------------------------------------------\n\n')
    print(request.headers.get('User-Agent'))
    print('\n\n------------------------------------------------\n\n')
    print(request.referrer)
    print('\n\n------------------------------------------------\n\n')
    print(request.method)
    print('\n\n------------------------------------------------\n\n')
    print(request.url)
    print('\n\n------------------------------------------------\n\n')
    print(request.headers)
    print('\n\n------------------------------------------------\n\n')
    print(request.accept_languages)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
