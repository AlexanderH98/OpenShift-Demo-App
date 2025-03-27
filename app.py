from flask import Flask, jsonify, request
import logging

# Initialize Flask app
app = Flask(__name__)

# Set up logging to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    app.logger.info("Home page was accessed")
    return "Welcome to the OpenShift Demo App!"

@app.route('/health')
def health():
    app.logger.info("Health check route was hit")
    return jsonify(status="OK", message="Application is healthy")

@app.route('/event', methods=['POST'])
def event():
    data = request.get_json()
    app.logger.info(f"Event received: {data}")
    return jsonify(status="received", data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
