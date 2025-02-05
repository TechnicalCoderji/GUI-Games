class GameBoard:
    # Define the possible winning combinations
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    def __init__(self):
        self.board = {(i,j):None for i in range(3) for j in range(3)}
        self.ready = False
        self.move_count = 0
        self.turn = "X"

    def connected(self):
        return self.ready
    
    def play(self, player, move):
        
        self.board[move] = player
        self.move_count += 1
        self.turn = "X" if self.turn == "O" else "O"
    
    def winner(self):
        # Check for a winner
        for combination in GameBoard.winning_combinations:
            values = [self.board[pos] for pos in combination]
            if values[0] is not None and values.count(values[0]) == len(values):
                return values[0]  # Return the player ('X' or 'O')

        # Check for a tie
        if all(value is not None for value in self.board.values()):
            return "Tie"

        # If there's no winner or tie, return None
        return None
        
    def reset_board(self):
        self.board = {(i,j):None for i in range(3) for j in range(3)}
        self.move_count = 0