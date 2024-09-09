from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['thesis']

@app.route('/add-code', methods=['POST'])
def add_entry():
    data = request.json
    result = db['codes'].insert_one(data)
    return jsonify({'success': True, 'codename': str(result.codename)})

@app.route('/is-code', methods=['GET'])
def get_entries():
    entries = list(db['codes'].find({}, {'codename': data['codename']}))
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(port=5000)
