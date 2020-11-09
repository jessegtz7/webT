from flask import Flask, jsonify
from usuarios import ausers

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "Hello there"})

@app.route('/users')
def usersHandler():
    return jsonify({"users": ausers})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)