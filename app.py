from flask import Flask, render_template, request
from models.entities.inputparser import InputParser

app = Flask(__name__)

intpars = InputParser()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        pass
    else:
        var = request.form['query_user']
        words = intpars.parser(var)
        return words
    
@app.errorhandler(404)
def page_not_found(error):
    return 'errors/404.html'

if __name__ == '__main__':
    app.run(debug=True, port=5000)