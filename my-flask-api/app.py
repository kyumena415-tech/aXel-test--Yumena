from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"pong": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
