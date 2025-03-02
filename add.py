# app.py
from flask import Flask, request, jsonify
from add import add

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_route():
    data = request.get_json()
    result = add(data['x'], data['y'])
    return jsonify({'result': result})

@app.route('/')
def home():
    return "Addition API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))