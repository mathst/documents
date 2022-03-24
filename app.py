from flask import Flask
import src.back as bk
import os

# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/a', methods=['GET'])
def funct():
    """ Function which is triggered in flask app """
    meses = 12
    result = bk.doing("ipca.xlsx",meses)
    return str(result)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>the result is in '/a'</h1>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port)



