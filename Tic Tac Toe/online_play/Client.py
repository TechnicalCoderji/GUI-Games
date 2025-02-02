import socket
import pickle
from gameboard import GameBoard

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 9999))

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        message = pickle.loads(data)
        if isinstance(message, str):
            print(message)
            if message == "Only one client connected":
                # Handle the situation where only one client is connected
                pass
            elif message == "Two clients connected":
                # Handle the situation where both clients are connected
                game_board = GameBoard("client initial state")
                data_to_send = pickle.dumps(game_board)
                client_socket.sendall(data_to_send)
        else:
            received_board = message
            print(f"Received from server: {received_board.board_state}")

            # Update game board or send a new one
            new_state = "updated state from client"
            game_board.update_board(new_state)
            data_to_send = pickle.dumps(game_board)
            client_socket.sendall(data_to_send)

    client_socket.close()

if __name__ == "__main__":
    client_program()