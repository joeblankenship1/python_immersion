from flask import Flask, send_file
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def get(self):
        return send_file('data/census_2010_ky.json')

api.add_resource(Data, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

