from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data for demo purposes
users = [
    {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
    {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
]

# GET /users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET /users/<id>
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((u for u in users if u['id'] == id), None)
    return jsonify(user) if user else ('User not found', 404)

# POST /users
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT /users/<id>
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = next((u for u in users if u['id'] == id), None)
    if user:
        user['name'] = data['name']
        user['email'] = data['email']
        return jsonify(user)
    return ('User not found', 404)

# DELETE /users/<id>
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if user:
        users.remove(user)
        return ('', 204)
    return ('User not found', 404)

if __name__ == '__main__':
    app.run(debug=True)
