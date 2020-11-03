from flask import abort, Flask, jsonify, request
from flask_restful import Resource, Api

from translation_engine import decode, encode

app = Flask(__name__)
api = Api(app)


class Encoder(Resource):
    def post(self):
        if not request.json or not 'message' in request.json:
            abort(400)
        msg = request.json['message']
        enc = encode(msg)
        return jsonify({"message": enc})

class Decoder(Resource):
    def post(self):
        if not request.json or not 'message' in request.json:
            abort(400)
        msg = request.json['message']
        try:
            dec = decode(msg)
        except ValueError as e:
            return str(e), 400
        return jsonify({'message': dec})

class Hello(Resource):
    def get(self):
        return 'Hello World!'

api.add_resource(Encoder, '/v1/encode')
api.add_resource(Decoder, '/v1/decode')
api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(threaded=True)
