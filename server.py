from flask import Flask, request, jsonify
import requests  # Used to send the webhook
import threading
import time

app = Flask(__name__)


def delayed_user_interaction(callback_url, data):
    time.sleep(1)  # Wait for a second
    # Send a webhook in response if callback_url is provided
    if callback_url:
        webhook_data = data
        webhook_data['response'] = 'i am server'
        requests.post(callback_url, json=webhook_data)


@app.route('/api/message', methods=['POST'])
def handle_message():
    # Get the message data and callback URL from the incoming request
    data = request.json
    message = data.get('message')
    callback_url = data.get('callback_url', None)

    # Process the message
    print(f"Received message: {message}")

    # Start a new thread to call user_interaction after a delay
    thread = threading.Thread(target=delayed_user_interaction, args=(callback_url, data))
    thread.start()

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000)
