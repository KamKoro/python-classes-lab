class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None
        }

    def print_board(self):
        b = self.board
        def cell(k):  # shows a blank if None
            return b[k] if b[k] is not None else ' '
        print(f"""
        A   B   C
    1)  {cell('a1')} | {cell('b1')} | {cell('c1')}
        ---+---+---
    2)  {cell('a2')} | {cell('b2')} | {cell('c2')}
        ---+---+---
    3)  {cell('a3')} | {cell('b3')} | {cell('c3')}
""")

    def print_message(self):
        if self.tie:
            print("It's a tie!")
        elif self.winner is not None:
            print(f"Player {self.winner} wins!")
        else:
            print(f"Player {self.turn}'s turn.")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        valid_keys = set(self.board.keys())
        while True:
            move = input("Enter a valid move (example: A1): ").strip().lower()
            if move not in valid_keys:
                print("That doesn't look right—use A/B/C with 1/2/3, e.g., A1 or c3.")
                continue
            if self.board[move] is not None:
                print("That space is taken. Choose another spot.")
                continue
            return move

    def check_for_winner(self):
        b = self.board
        lines = [
            # rows
            ('a1','b1','c1'), ('a2','b2','c2'), ('a3','b3','c3'),
            # cols
            ('a1','a2','a3'), ('b1','b2','b3'), ('c1','c2','c3'),
            # diagonals
            ('a1','b2','c3'), ('c1','b2','a3')
        ]
        for a, c, d in lines:
            if b[a] and b[a] == b[c] == b[d]:
                self.winner = b[a]
                return True
        return False

    def check_for_tie(self):
        if self.winner is None and all(v is not None for v in self.board.values()):
            self.tie = True
            return True
        return False

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        while self.winner is None and not self.tie:
            self.render()
            move = self.get_move()
            self.board[move] = self.turn

            if self.check_for_winner() or self.check_for_tie():
                self.render()
                break

            self.switch_turn()
            # Optional: self.render() here if you want to show the board immediately after switching

if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
