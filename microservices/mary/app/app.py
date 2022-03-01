from flask import Flask
from flask_restful import Resource,Api
import socket
import datetime

app = Flask(__name__)
api = Api(app)

class Welcome(Resource):
    def get(self):
        hostname = socket.gethostname()
        msg = {'message': f'Welcome to microservice! from {hostname}'}

        e = datetime.datetime.now()
        if e.hour < 11:
            msg = {"mary_says":"good_morning"}
        elif e.hour < 17:
            msg = {"mary_says": "good_afternoon"}
        elif e.hour < 24:
            msg = {"mary_says": "good_evening"}
        return msg


api.add_resource(Welcome, '/')

if __name__ == '__main__':
    app.run(debug=True,port=5051,host="0.0.0.0")