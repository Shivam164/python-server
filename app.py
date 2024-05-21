from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST", "GET"])
def handleRequest():
    body = request.get_json()
    print(body)
    return jsonify({"message": "recieved"}), 200

@app.route("/webhook/:id", methods=["POST", "GET"])
def handleRequest():
    print(id)
    body = request.get_json()
    print(body)
    return jsonify({"message": "recieved"}), 200

# if __name__ == '__main__':
#     app.debug = True
#     app.run('0.0.0.0', port=4100)