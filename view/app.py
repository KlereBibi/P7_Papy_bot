from flask import Flask, render_template, request

import sys
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

app=Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")