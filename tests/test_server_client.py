from time import sleep

from main import db
from server_communication import send_message_to_mock_server


def test_server_client():
    print('round 1')
    for user in db.get_all_users():
        input()
        # Wait for the server to start and then send a message
        welcome_attachment = {
            "actions": [
                {
                    "name": "show_coupon",
                    "text": "Yes! Show me coupon",
                    "type": "button"
                },
                {
                    "name": "no_thanks",
                    "text": "No, thanks",
                    "type": "button"
                }
            ]
        }
        data = {
            "user_id": user.user_id,
            "callback_url": "http://localhost:6000/webhook/callback",
            "text": f"Welcome to the demo promotional flow, {user.name}! Are you interested in our coupon promotion?",
            "attachments": welcome_attachment
        }

        send_message_to_mock_server(data)

    sleep(1)
    print('round 2')
    for user in db.get_all_users():
        input()

        # Wait for the server to start and then send a message
        coupon_attachment = {
            "actions": [
                {
                    "name": "reveal_coupon",
                    "text": "Reveal Coupon",
                    "type": "button",
                    "url": "http://example.com/coupon/reveal"
                }
            ]
        }

        data = {
            "user_id": user.user_id,
            "callback_url": "http://localhost:6000/webhook/callback",
            "text": "Here is our unique promotional coupon! 10% off. Limit 1 per customer.",
            "attachments": coupon_attachment
        }

        send_message_to_mock_server(data)

    sleep(1)
    print('round 3')
    for user in db.get_all_users():
        input()

        # Wait for the server to start and then send a message
        media_attachment = {
            "image_url": "https://example.com/goodbye-image.jpg"
        }

        data = {
            "user_id": user.user_id,
            "callback_url": "http://localhost:6000/webhook/callback",
            "text": "No worries! Have a nice day!",
            "attachments": media_attachment
        }

        send_message_to_mock_server(data)
