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

    data2={
        "event_type": "link_click",
        "user_id": 'user_id',
        "link_url": 'clicked_link_url'
    }
    requests.post(callback_url, json=data2)

    data3={
    "event_type": "button_click",
    "user_id": 'user_id',
    "button_name": 'clicked_button_name'
    }
    requests.post(callback_url, json=data3)

    # Send a webhook in response if callback_url is provided
    if callback_url:
        webhook_data = data
        webhook_data['response'] = 'i am server'
        requests.post(callback_url, json=webhook_data)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000)
