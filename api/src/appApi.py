from flask import Flask
import back

class FlaskAppWrapper(object):

    def __init__(self, app, **configs):
        self.app = app
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)

    def run(self, **kwargs):
        self.app.run(**kwargs)

flask_app = Flask(__name__)

app = FlaskAppWrapper(flask_app)

def funct():
    """ Function which is triggered in flask app """
    meses = 12
    result = back.doing("ipca.xlsx",meses)
    return str(result)

app.add_endpoint('/', 'index', funct, methods=['GET'])
if __name__ == "__main__":
    app.run(debug=True)
