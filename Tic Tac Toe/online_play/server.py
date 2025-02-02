import socket
import threading
import pickle
from gameboard import GameBoard

clients = []

def broadcast(message):
    for client in clients:
        client.sendall(message)

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
            broadcast(data_to_send)
        except:
            break

    clients.remove(client_socket)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(2)
    print("Server listening on port 9999")

    game_board = GameBoard("O","initial state")
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        clients.append(client_socket)

        if len(clients) == 1:
            message = pickle.dumps((game_board.game_board,"Only one client connected"))
            client_socket.sendall(message)
        elif len(clients) == 2:
            message = pickle.dumps((game_board.game_board,"Two clients connected"))
            broadcast(message)

        client_handler = threading.Thread(target=handle_client, args=(client_socket, game_board))
        client_handler.start()

if __name__ == "__main__":
    start_server()