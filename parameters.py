from datetime import datetime

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
