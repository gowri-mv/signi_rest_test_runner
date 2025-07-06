from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = {"id": len(users) + 1, "name": data.get("name")}
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
