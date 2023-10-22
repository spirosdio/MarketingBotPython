from datetime import datetime
from random import random

from flask import Flask, request, jsonify
import requests  # Used to send the webhook
import threading
import time

app = Flask(__name__)

sleep_time = 0.1


def delayed_user_interaction(callback_url, data):
    time.sleep(sleep_time)  # Wait for a second
    if random() < 0.8:
        message_read_answer = {
            "event_type": "message_read",
            "user_id": data['user_id'],
            "interaction_timestamp": datetime.utcnow().timestamp()
        }
        requests.post(callback_url, json=message_read_answer)

        time.sleep(sleep_time)  # Wait for a second
        try:
            if len(data['attachments']['actions'])==2:
                if random() < 0.8:
                    if random() < 0.66:
                        welcome_attachment_answer = {
                            "event_type": "button_click",
                            "user_id": data['user_id'],
                            "button_name": 'show_coupon'
                        }
                    else:
                        welcome_attachment_answer = {
                            "event_type": "button_click",
                            "user_id": data['user_id'],
                            "button_name": 'no_thanks'
                        }

                    requests.post(callback_url, json=welcome_attachment_answer)

            if len(data['attachments']['actions']) == sleep_time:
                if random() < 0.8:
                    coupon_attachment_answer = {
                        "event_type": "link_click",
                        "user_id": data['user_id'],
                        "link_url": data['attachments']['actions'][0]['url']
                    }
                    requests.post(callback_url, json=coupon_attachment_answer)
        except:
            pass

@app.route('/api/message', methods=['POST'])
def handle_message():
    # Get the message data and callback URL from the incoming request
    data = request.json
    callback_url = data.get('callback_url', None)

    # Process the message
    print(f"Received message: {data}")

    # Start a new thread to call user_interaction after a delay
    thread = threading.Thread(target=delayed_user_interaction, args=(callback_url, data))
    thread.start()

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000)
