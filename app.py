"""This module contains the framwork flask to run the application"""

from flask import Flask, render_template, request, jsonify

from controller.control import Control

def create_app(config={"TESTING": False}):

    """this method allows you to create a web page.
    return : HTML page
             dictionnary element transform in javascript langage
             the application"""

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

""" APP = create_app({"TESTING": False})

if __name__ == '__main__':
    APP.run() """