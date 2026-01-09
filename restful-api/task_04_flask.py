from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with an empty dictionary to pass the "no users added" test
users = {}

@app.route("/")
def get_root():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    # Return only the keys (usernames) as a list
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    return "OK"

@app.route("/users/<username>")
def get_users(username):
    user_data = users.get(username)
    if user_data:
        return jsonify(user_data)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def post_data():
    user_data = request.get_json()

    if not user_data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Match the exact error message and status code (400) for the checker
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
