from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId



app = Flask(__name__)

CORS(app)  # Enable CORS for all routes

# Connect to MongoDB
client = MongoClient("mongodb://mongodb:27017/")  # Connect to the MongoDB service
db = client['userdb']  # Database
users_collection = db['users']  # Collection

@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}))
    for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string for JSON
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    result = users_collection.insert_one(user_data)
    user_data['_id'] = str(result.inserted_id)  # Add inserted _id to the response
    return jsonify(user_data), 201

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = users_collection.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count == 1:
        return '', 204  # Successfully deleted
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
