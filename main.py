from test_server_client import test_server_client
from user_database import UserDatabase
import threading
from server_communication import run_client_server

if __name__ == "__main__":
    # Start the client's server in a separate thread
    threading.Thread(target=run_client_server).start()

    db = UserDatabase()
    db.create_user('spiros', 'diochnos', 1, '26')
    db.create_user('vaso', 'kollia', 2, '27')
    db.create_user('angelos', 'todri', 3, '28')

    # test_server_client()

