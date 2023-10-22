from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)



data2 = {
    "event_type": "link_click",
    "user_id": 'user_id',
    "link_url": 'clicked_link_url'
}


data3 = {
    "event_type": "button_click",
    "user_id": 'user_id',
    "button_name": 'clicked_button_name'
}


@app.route('/slack-webhook', methods=['POST'])
def slack_webhook_receiver():
    data = request.get_json()
    text = data.get('text', '')

    response_attachments = build_message_attachments()

    # Send a response back to the Slack channel
    return send_slack_message(data['channel'], text, response_attachments)

     # jsonify({})


def build_message_attachments():
    # Attachments for the message
    image_url = "https://example.com/image.jpg"
    link_url = "https://example.com/link"

    attachments = [
        {
            "text": "Here's an image:",
            "fallback": "Image not supported",
            "image_url": image_url
        },
        {
            "text": "Please choose an option:",
            "fallback": "Options not supported",
            "callback_id": "option_selection",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "option",
                    "text": "Option 1",
                    "type": "button",
                    "value": "option_1"
                },
                {
                    "name": "option",
                    "text": "Option 2",
                    "type": "button",
                    "value": "option_2"
                }
            ]
        },
        {
            "text": "Or, visit this link:",
            "fallback": "Link not supported",
            "actions": [
                {
                    "type": "button",
                    "text": "Visit Link",
                    "url": link_url
                }
            ]
        }
    ]

    return attachments


def send_slack_message(channel, text, attachments):
    slack_api_url = "https://slack.com/api/chat.postMessage"
    slack_bot_token = "YOUR_BOT_TOKEN"

    message_payload = {
        "channel": channel,
        "text": text,
        "attachments": attachments
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {slack_bot_token}"
    }

    return message_payload
    response = requests.post(slack_api_url, data=json.dumps(message_payload), headers=headers)

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")


if __name__ == '__main__':
    app.run(debug=True)
