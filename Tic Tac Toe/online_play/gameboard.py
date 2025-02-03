import socket
import pickle
import threading

class TicTacToe:

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.you = "O"
        self.opponent = "X"
        self.winner = None

        self.counter = 0

    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host,port))
        server.listen(1)

        self.you = "O"
        self.opponent = "X"

        client, addr = server.accept()

        threading.Thread(target=self.handle_connection, args=(client,)).start()
        server.close()

    def connect_to_game(self ,host, port):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        self.you = "X"
        self.opponent = "O"

        threading.Thread(target=self.handle_connection, args=(client,)).start()

    def handle_connection(self, client):

        while True:
            if self.turn == self.you:
                move = (1,2)
                
                self.apply_move(move.split(","),self.you)
                self.turn = self.opponent
                client.send(pickle.dumps(move))

            else:
                data = pickle.loads(client.recv(128))
                if not data:
                    break
                else:
                    self.apply_move(data, self.opponent)
                    self.turn = self.you

        client.close()

    def apply_move(self, move, player):
        
        self.counter += 1
        self.board[move[0]][move[1]] = player

if __name__ == "main":
    pass