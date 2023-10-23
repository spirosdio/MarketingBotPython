from parameters import user_node_dict, create_welcoming_message, create_coupon_message, create_media_message
from server_communication import run_client_server, send_message_to_mock_server
from tree import Data, TreeNode
from user_database import UserDatabase
import threading

if __name__ == "__main__":
    # Start the client's server in a separate thread
    threading.Thread(target=run_client_server).start()

    db = UserDatabase()
    db.create_user('spiros', 'diochnos', 1, '26')
    db.create_user('vaso', 'kollia', 2, '27')
    db.create_user('angelos', 'todri', 3, '28')

    # Creating data instances
    data_root = Data(create_welcoming_message)
    data_child1 = Data(create_coupon_message, "show_coupon")
    data_child2 = Data(create_media_message, "no_thanks")

    # Creating the tree nodes with data instances
    root = TreeNode(data_root)
    child1 = TreeNode(data_child1)
    child2 = TreeNode(data_child2)

    # Building the tree structure
    root.add_child(child1)
    root.add_child(child2)

    #a dict that has a user as key and the root node as value
    for user in db.get_all_users():
        user_node_dict[user] = root
        send_message_to_mock_server(root.data.json(user))

    # Displaying the tree
    root.display()
