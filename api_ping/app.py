from flask import Flask, jsonify
from flask_cors import CORS  # 追加

app = Flask(__name__)
CORS(app)  # 追加

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"pong": True})

if __name__ == '__main__':
    app.run(debug=True)
