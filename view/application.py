from flask import Flask, render_template, request, jsonify

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from controller.control import Control

app=Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/ajax', methods=['POST'])
def ajax():
    user_text = request.form["userText"]
    mycontroller = Control()
    article = mycontroller.search_article(user_text) 
    print(article)
    return jsonify(article)
    
    