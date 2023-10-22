from flask import Flask, request, jsonify
import requests  # Used to send the webhook

app = Flask(__name__)

@app.route('/api/message', methods=['POST'])
def handle_message():
    # Get the message data and callback URL from the incoming request
    data = request.json
    message = data.get('message')
    callback_url = data.get('callback_url', None)

    # Process the message
    print(f"Received message: {message}")

    # Send a webhook in response if callback_url is provided
    if callback_url:
        webhook_data = {
            "response": f"Received your message: {message}"
        }
        requests.post(callback_url, json=webhook_data)

    # Respond to the incoming request
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000)
