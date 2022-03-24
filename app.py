from flask import Flask
import src.back as back

# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/a', methods=['GET'])
def funct():
    """ Function which is triggered in flask app """
    meses = 12
    result = back.doing("ipca.xlsx",meses)
    return str(result)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>the result is in '/a'</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=8000)



