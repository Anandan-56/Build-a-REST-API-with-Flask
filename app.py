from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
users = {}      # { id: { "id": id, "name": "...", "email": "..." } }
next_id = 1     # Auto-increment user ID


@app.route("/users", methods=["GET"])
def get_users():
    """Get all users"""
    return jsonify(list(users.values())), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Get a single user by ID"""
    user = users.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


@app.route("/users", methods=["POST"])
def create_user():
    """Create a new user"""
    global next_id

    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "name and email are required"}), 400

    user = {
        "id": next_id,
        "name": data["name"],
        "email": data["email"]
    }

    users[next_id] = user
    next_id += 1

    return jsonify(user), 201  # 201 = Created


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update an existing user"""
    user = users.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Update only provided fields
    if "name" in data:
        user["name"] = data["name"]
    if "email" in data:
        user["email"] = data["email"]

    users[user_id] = user
    return jsonify(user), 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a user"""
    user = users.pop(user_id, None)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": f"User {user_id} deleted"}), 200


if __name__ == "__main__":
    # debug=True is useful in development
    app.run(debug=True)
