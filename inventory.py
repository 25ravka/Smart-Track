from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "inventory_data.json"

# Save inventory data
@app.route('/save_inventory', methods=['POST'])
def save_inventory():
    data = request.get_json()

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({"message": f"Inventory saved successfully! {len(data)} items saved."})

# Load inventory data
@app.route('/get_inventory', methods=['GET'])
def get_inventory():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
