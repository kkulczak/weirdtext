from flask import Flask, request
from flask_restful import Resource, Api

from translation_engine import decode, encode

app = Flask(__name__)
api = Api(app)


class Encoder(Resource):
    def post(self):
        msg = str(request.data)
        enc = encode(msg)
        return enc


class Decoder(Resource):
    def post(self):
        msg = str(request.data)
        try:
            dec = decode(msg)
        except ValueError as e:
            return str(e), 400
        return dec


api.add_resource(Encoder, '/v1/encode')
api.add_resource(Decoder, '/v1/decode')

if __name__ == '__main__':
    app.run(debug=True)
