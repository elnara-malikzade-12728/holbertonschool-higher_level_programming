from flask import Flask, jsonify, request

app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def get_root():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    return "OK"

@app.route("/users/<username>")
def get_users(username):
    # 1. Check if the user exists in the dictionary
    user_data = users.get(username)

    if user_data:
        # 2. Return the full user object (dictionary)
        return jsonify(user_data)
    else:
        # 3. Return an error if the user is not found
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def post_data():
    user_data = request.get_json()

    # Ensure JSON was provided
    if not user_data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Safety check: username in users
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Save the user data
    users[username] = user_data

    # Return success message and the user object with 201 Created
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run(port=5000)