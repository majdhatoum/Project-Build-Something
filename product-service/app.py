from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId



app = Flask(__name__)

CORS(app)  # Enable CORS for all routes

# Connect to MongoDB
client = MongoClient("mongodb://mongodb:27017/")  # Connect to the MongoDB service
db = client['productdb']  # Database
products_collection = db['products']  # Collection

@app.route('/products', methods=['GET'])
def get_products():
    products = list(products_collection.find({}))
    for product in products:
        product['_id'] = str(product['_id'])  # Convert ObjectId to string for JSON
    return jsonify(products), 200

@app.route('/products', methods=['POST'])
def create_product():
    product_data = request.json
    result = products_collection.insert_one(product_data)
    product_data['_id'] = str(result.inserted_id)  # Add inserted _id to the response
    return jsonify(product_data), 201

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    result = products_collection.delete_one({'_id': ObjectId(product_id)})
    if result.deleted_count == 1:
        return '', 204  # Successfully deleted
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
