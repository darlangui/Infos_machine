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

def info_system():
    versao_sistema = platform.version()
    arquitetura = platform.architecture()
    processador = platform.processor()
    cpu_percent = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    total_mem = round(mem.total / (1024 * 1024 * 1024), 2)
    available_mem = round(mem.available / (1024 * 1024 * 1024), 2)
    used_mem = round(mem.used / (1024 * 1024 * 1024), 2)
    print(f"Nome do sistema operacional: {platform.system()}")
    print(f"Versão do sistema operacional: {versao_sistema}")
    print(f"Versão do sistema operacional: {platform.release()}")
    print(f"Arquitetura da máquina: {platform.machine()}")
    print(f"Arquitetura: {arquitetura}")
    print(f"Processador: {processador}")
    print(f"Uso de CPU: {cpu_percent}%")
    print(f"Memória total: {total_mem} GB")
    print(f"Memória disponível: {available_mem} GB")
    print(f"Memória usada: {used_mem} GB")
    print(f"Nome do usuário: ", {getpass.getuser()})
@app.route('/')
def index():  # put application's code here
    info(search_ip(request.remote_addr))
    print('\n\n------------------------------------------------\n\n')
    info_system()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
