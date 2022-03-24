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
    return str(result)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)



