from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for demo purposes
data_entries = []

@app.route('/update', methods=['GET'])
def update():
    moisture = request.args.get('moisture')
    temperature = request.args.get('temperature')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if moisture and temperature:
        # Store only the latest 10 readings for simplicity
        if len(data_entries) >= 10:
            data_entries.pop(0)
        data_entries.append({
            "moisture": int(moisture),
            "temperature": int(temperature),
            "timestamp": timestamp
        })
    return "Data Received", 200

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_entries)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)