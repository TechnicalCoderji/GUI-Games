import socket
import pickle

class TicTacToe:
    
    # List of winning combinations
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],  # Top row
        [(1, 0), (1, 1), (1, 2)],  # Middle row
        [(2, 0), (2, 1), (2, 2)],  # Bottom row
        [(0, 0), (1, 0), (2, 0)],  # Left column
        [(0, 1), (1, 1), (2, 1)],  # Middle column
        [(0, 2), (1, 2), (2, 2)],  # Right column
        [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
        [(0, 2), (1, 1), (2, 0)],  # Diagonal from top-right to bottom-left
    ]

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.you = "O"
        self.opponent = "X"
        self.winner = None

        self.counter = 0

    def host_game(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host,port))
        self.server.listen(1)

        self.you = "O"
        self.opponent = "X"

        client, addr = self.server.accept()

    def connect_to_game(self ,host, port):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        self.you = "X"
        self.opponent = "O"

    def handle_connection(self, client, move):

        if self.turn == self.you:

            self.apply_move(move,self.you)
            self.turn = self.opponent
            client.send(pickle.dumps(move))

        else:
            data = pickle.loads(client.recv(128))
            if not data:
                return False
            else:
                self.apply_move(data, self.opponent)
                self.turn = self.you

        # client.close()

    def apply_move(self, move, player):
        
        self.counter += 1
        self.board[move[0]][move[1]] = player