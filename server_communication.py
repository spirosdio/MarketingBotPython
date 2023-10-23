import requests
from flask import Flask, request, jsonify

from parameters import user_node_dict
from user_database import UserDatabase

app = Flask(__name__)


def run_client_server():
    app.run(port=6000)


def handle_answer_received(userdb,  data):
    print(f"Received answer from user {userdb.name} , {data}")
    if data['event_type'] == 'message_read':
        print(f"User {userdb.name} {userdb.surname} read the message at {data['interaction_timestamp']}")
        return

    if data['event_type'] == 'link_click':
        print(f"User {userdb.name} {userdb.surname} clicked the link!!!!!")
        return

    node = user_node_dict[userdb]
    for child in node.children:
        if child.data.button_name_of_origin == data['button_name']:
            node = child
            send_message_to_mock_server(node.data.json(userdb))


@app.route('/webhook/callback', methods=['POST'])
def handle_webhook():
    data = request.json
    db = UserDatabase()
    handle_answer_received(db.get_user(data['user_id']), data)
    return jsonify({"status": "success"})


def send_message_to_mock_server(data):
    # The URL of the server endpoint
    server_url = "http://localhost:5000/api/message"

    # Make the POST request
    response = requests.post(server_url, json=data)

    # Check the response
    if response.status_code == 200:
        print(f"Server responded with: {response.json()}")
    else:
        print(f"Failed to send message. Server responded with status code: {response.status_code}")
