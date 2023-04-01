from flask import Flask, render_template
import getpass
import json
import os
import platform
import psutil
import requests

app = Flask(__name__)



@app.route('/')
def index():  # put application's code here

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
