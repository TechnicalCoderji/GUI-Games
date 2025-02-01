import socket
import threading
import pickle

class GameBoard:
    def __init__(self, board_state):
        self.board_state = board_state

    def update_board(self, new_state):
        self.board_state = new_state

def handle_client(client_socket, game_board):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            received_board = pickle.loads(data)
            print(f"Received: {received_board.board_state}")

            game_board.update_board(received_board.board_state)
            data_to_send = pickle.dumps(game_board)
            client_socket.sendall(data_to_send)
        except:
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Server listening on port 9999")

    game_board = GameBoard("initial state")
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, game_board))
        client_handler.start()

if __name__ == "__main__":
    start_server()