from flask import Flask, request, jsonify, render_template
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

JSON_FILE = "data1.json"

if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    data = request.json.get("text", "")

    with open(JSON_FILE, "r") as f:
        current = json.load(f)

    current.append(data)

    with open(JSON_FILE, "w") as f:
        json.dump(current, f, indent=4)

    return jsonify({"status": "Successfully Done"})

@app.route("/all")
def all_data():
    with open(JSON_FILE, "r") as f:
        current = json.load(f)

    return jsonify(current)

if __name__ == "__main__":
    app.run()