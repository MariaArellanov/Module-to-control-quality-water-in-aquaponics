from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enables Cross-Origin Resource Sharing for the Dashboard

# Data structure to store the latest sensor readings
# In a production environment, this would be replaced by a database (SQL/NoSQL)
system_data = {
    "water": {"temp": "0"},
    "ambient": {"temp": "0"},
    "flow": {"rate": "0"}
}

@app.route('/')
def index():
    return "Aquaponics Monitoring API is online."

# --- POST ENDPOINTS (Receiving data from Raspberry Pi) ---

@app.route('/water', methods=['POST'])
def update_water():
    data = request.get_json()
    system_data["water"]["temp"] = data.get("temp", "0")
    return jsonify({"status": "success", "message": "Water temperature updated"}), 200

@app.route('/ambient', methods=['POST'])
def update_ambient():
    data = request.get_json()
    system_data["ambient"]["temp"] = data.get("temp", "0")
    return jsonify({"status": "success", "message": "Ambient temperature updated"}), 200

@app.route('/flow', methods=['POST'])
def update_flow():
    data = request.get_json()
    system_data["flow"]["rate"] = data.get("flow", "0")
    return jsonify({"status": "success", "message": "Flow rate updated"}), 200

# --- GET ENDPOINTS (Providing data to the Dashboard) ---

@app.route('/water', methods=['GET'])
def get_water():
    return jsonify(system_data["water"])

@app.route('/ambient', methods=['GET'])
def get_ambient():
    return jsonify(system_data["ambient"])

@app.route('/flow', methods=['GET'])
def get_flow():
    return jsonify(system_data["flow"])

if __name__ == '__main__':
    # host='0.0.0.0' allows access from other devices on the same network
    app.run(host='0.0.0.0', port=5000, debug=True)