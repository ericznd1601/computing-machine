from flask import Flask, request, jsonify, send_from_directory
import os
from microsservice.checkRoad import get_surface_type

app = Flask(__name__, static_folder="../frontend", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/script.js")
def js():
    return send_from_directory(app.static_folder, "script.js")

@app.route("/api/check", methods=["POST"])
def check_surface():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")

    if lat is None or lon is None:
        return jsonify({"error": "Missing coordinates"}), 400

    surface_type = get_surface_type(lat, lon)
    return jsonify({"surface": surface_type})
