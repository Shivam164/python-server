from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST", "GET"])
def handleRequest():
    body = request.get_json()
    print(body)
    return jsonify({"message": "recieved"}), 200