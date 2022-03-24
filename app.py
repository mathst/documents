from flask import Flask, request
import back as bk
import os

app = Flask(__name__)

@app.route('/a', methods=['GET'])
def a():  
    meses = 12
    result = bk.doing("ipca.xlsx",meses)
    return str(result)

@app.route('/b', methods=['GET'])
def b():
    meses = request.args.get('meses')
    file = bk.resquestBank()
    result = bk.doing(file,meses)
    return str(result)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>the result is in '/a'</h1>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port)



