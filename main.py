from user_database import UserDatabase, User
import threading
from time import sleep
from parameters import welcome_attachment
from server_communication import run_client_server, send_message_to_server

if __name__ == "__main__":
    # Start the client's server in a separate thread
    threading.Thread(target=run_client_server).start()

    db = UserDatabase()
    db.create_user('spiros', 'diochnos', 1, '26')
    db.create_user('vaso', 'kollia', 2, '27')
    db.create_user('angelos', 'todri', 3, '28')

    print('round 1')

    for user in db.get_all_users():
        # Wait for the server to start and then send a message
        user_message = input()
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

        send_message_to_server(data)

    sleep(1.51)
    print('round 2')

    for user in db.get_all_users():
        # Wait for the server to start and then send a message
        user_message = input()
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


        send_message_to_server(data)

    sleep(1.51)
    print('round 3')

    for user in db.get_all_users():
        # Wait for the server to start and then send a message
        user_message = input()
        media_attachment = {
            "image_url": "https://example.com/goodbye-image.jpg"
        }

        data = {
            "user_id": user.user_id,
            "callback_url": "http://localhost:6000/webhook/callback",
            "text": "No worries! Have a nice day!",
            "attachments": media_attachment
        }

        send_message_to_server(data)

