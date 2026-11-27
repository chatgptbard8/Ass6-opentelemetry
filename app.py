from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        service="Assignment 6 OpenTelemetry Demo",
        endpoints=["/success", "/slow", "/error", "/health"]
    )

@app.route("/success")
def success():
    return jsonify(status="success", message="Request completed successfully"), 200

@app.route("/slow")
def slow():
    time.sleep(2)
    return jsonify(status="success", message="Slow request completed after 2 seconds"), 200

@app.route("/error")
def error():
    return jsonify(status="error", message="Simulated application failure"), 500

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
