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
media_attachment = {
    "text": "No worries! Have a nice day!",
    "image_url": "https://example.com/goodbye-image.jpg"
}
