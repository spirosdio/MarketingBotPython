import requests
from flask import Flask, request, jsonify

from change_this_name import handle_answer_received

app = Flask(__name__)


def run_client_server():
    app.run(port=6000)


@app.route('/webhook/callback', methods=['POST'])
def handle_webhook():
    data = request.json
    handle_answer_received(data)
    return jsonify({"status": "success"})


def send_message_to_mock_server(data):
    # The URL of the server endpoint
    server_url = "http://localhost:5000/api/message"

    # Make the POST request
    response = requests.post(server_url, json=data)

    # Check the response
    if response.status_code == 200:
        print(f"Server responded with: {response.json()}")
    else:
        print(f"Failed to send message. Server responded with status code: {response.status_code}")
