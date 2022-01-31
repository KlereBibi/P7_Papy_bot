from flask import Flask, render_template, request, jsonify

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from controller.control import Control

def create_app(config):
    
    app = Flask(__name__)
    app.config.from_object(config)
    
    @app.route('/', methods=['GET'])
    def home():
        return render_template("index.html")

    @app.route('/ajax', methods=['POST'])
    def ajax():
        user_text = request.form["userText"]
        mycontroller = Control()
        article = mycontroller.search_article(user_text) 
        return jsonify(article)

    return app

