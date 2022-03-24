import logging
from flask import Flask
import back

# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def funct():
    """ Function which is triggered in flask app """
    meses = 12
    result = back.doing("ipca.xlsx",meses)
    return str(result) | logging.error()

# A welcome message to test our server
@app.route('/')
def index():
    """ Function which is triggered in flask app """
    meses = 12
    result = back.doing("ipca.xlsx",meses)
    return f'<h1>{str(result) | logging.error()}</h1>'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
