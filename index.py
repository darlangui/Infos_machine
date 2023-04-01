from flask import Flask, render_template, request
import getpass
import json
import os
import platform
import psutil
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

@app.route('/')
def index():  # put application's code here
    info(search_ip(request.remote_addr))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
