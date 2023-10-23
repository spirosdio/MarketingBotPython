from datetime import datetime

jpg = "https://example.com/goodbye-image.jpg"


welcome_attachment = {
    "text": "Welcome to the demo promotional flow, John! Are you interested in our coupon promotion?",
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
welcome_attachment_answer_1 = {
    "event_type": "button_click",
    "user_id": 'user_id',
    "button_name": 'show_coupon'
}
welcome_attachment_answer_2 = {
    "event_type": "button_click",
    "user_id": 'user_id',
    "button_name": 'no_thanks'
}
coupon_attachment = {
    "text": "Here is our unique promotional coupon! 10% off. Limit 1 per customer.",
    "actions": [
        {
            "name": "reveal_coupon",
            "text": "Reveal Coupon",
            "type": "button",
            "url": "http://example.com/coupon/reveal"
        }
    ]
}
coupon_attachment_answer = {
    "event_type": "link_click",
    "user_id": 'user_id',
    "link_url": 'http://example.com/coupon/reveal'
}
media_attachment = {
    "text": "No worries! Have a nice day!",
    "image_url": "https://example.com/goodbye-image.jpg"
}
message_read_answer = {
    "event_type": "message_read",
    "user_id": 'user_id',
    "interaction_timestamp": datetime.utcnow().timestamp()
}


user_node_dict = {}


def create_welcoming_message(userdb):
    welcoming_attachment = {
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
    return {
        "user_id": userdb.user_id,
        "callback_url": "http://localhost:6000/webhook/callback",
        "text": f"Welcome to the demo promotional flow, {userdb.name}! Are you interested in our coupon promotion?",
        "attachments": welcoming_attachment
    }


def create_coupon_message(userdb):
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
    return {
        "user_id": userdb.user_id,
        "callback_url": "http://localhost:6000/webhook/callback",
        "text": "Here is our unique promotional coupon! 10% off. Limit 1 per customer.",
        "attachments": coupon_attachment
    }


def create_media_message(userdb):
    media_attachment = {
        "image_url": jpg
    }
    return {
        "user_id": userdb.user_id,
        "callback_url": "http://localhost:6000/webhook/callback",
        "text": "No worries! Have a nice day!",
        "attachments": media_attachment
    }


stats = {
    'users': 0,
    'positive_responses': 0,
    'negative_responses': 0,
    'coupon_reveals': 0,
    'messages_read': 0
}
