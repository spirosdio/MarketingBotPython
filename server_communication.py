from pprint import pprint

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


def run_client_server():
    app.run(port=6000)


@app.route('/webhook/callback', methods=['POST'])
def handle_webhook():
    data = request.json
    pprint(data)
    return jsonify({"status": "success"})


def send_message_to_server(message):
    # The URL of the server endpoint
    server_url = "http://localhost:5000/api/message"

    # The data to send in the POST request
    data = {
        "message": message,
        "callback_url": "http://localhost:6000/webhook/callback"
    }

    # Make the POST request
    response = requests.post(server_url, json=data)

    # Check the response
    if response.status_code == 200:
        print(f"Server responded with: {response.json()}")
    else:
        print(f"Failed to send message. Server responded with status code: {response.status_code}")
