class Game:
    def __init__(self):
        # Session-wide stats
        self.score = {'X': 0, 'O': 0, 'ties': 0}
        # Who starts the next game (we alternate for fairness)
        self.starting_player = 'X'
        # Set up the first board
        self.reset_board()

    # ========== Core state ==========
    def reset_board(self):
        self.turn = self.starting_player
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None
        }

    # ========== Rendering ==========
    def print_board(self):
        b = self.board
        def cell(k): return b[k] if b[k] is not None else ' '
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
            print(f"It's player {self.turn}'s turn.")

    def render(self):
        self.print_board()
        self.print_message()

    # ========== Input & Rules ==========
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
            ('a1','b1','c1'), ('a2','b2','c2'), ('a3','b3','c3'),   # rows
            ('a1','a2','a3'), ('b1','b2','b3'), ('c1','c2','c3'),   # cols
            ('a1','b2','c3'), ('c1','b2','a3')                      # diagonals
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

    # ========== One full game ==========
    def play_one_round(self):
        print("Welcome to Tic Tac Toe!")
        while self.winner is None and not self.tie:
            self.render()
            move = self.get_move()
            self.board[move] = self.turn

            if self.check_for_winner() or self.check_for_tie():
                self.render()
                break

            self.switch_turn()

        # Update records
        if self.winner:
            self.score[self.winner] += 1
        else:
            self.score['ties'] += 1

        # Show records after each game
        print(f"\nRecord — X: {self.score['X']} | O: {self.score['O']} | Ties: {self.score['ties']}\n")

    # ========== Play-again loop ==========
    def ask_play_again(self):
        while True:
            ans = input("Play again? (y/n): ").strip().lower()
            if ans in ('y', 'yes'):
                return True
            if ans in ('n', 'no'):
                return False
            print("Please enter 'y' or 'n'.")

    def play_game(self):
        while True:
            self.play_one_round()
            if not self.ask_play_again():
                print("Thanks for playing!")
                print(f"Final record — X: {self.score['X']} | O: {self.score['O']} | Ties: {self.score['ties']}")
                break
            # Alternate starting player for the next round and reset the board
            self.starting_player = 'O' if self.starting_player == 'X' else 'X'
            self.reset_board()


if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
