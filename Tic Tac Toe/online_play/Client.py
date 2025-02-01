# gameboard.py

class GameBoard:
    def __init__(self, board_state):
        self.board_state = board_state

    def update_board(self, new_state):
        self.board_state = new_state