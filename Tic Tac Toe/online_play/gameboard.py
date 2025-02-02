class GameBoard:
    def __init__(self, sign, state):
        self.sign = sign
        self.game_board = {(i, j): None for i in range(3) for j in range(3)}
        self.state = state

    def update_board(self, board, state):
        self.game_board = board
        self.state = state