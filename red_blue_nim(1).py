import argparse

class MarbleGame:
    def __init__(self, red_count, blue_count, game_type, starting_player, ai_depth):
        self.red_count = red_count
        self.blue_count = blue_count
        self.game_type = game_type
        self.starting_player = starting_player
        self.ai_depth = ai_depth
        self.marbles = {"red": red_count, "blue": blue_count}

    def play_game(self):
        current_player = self.starting_player
        print(f"Game start! Type: {self.game_type}, Starting player: {current_player}")
        
        while not self.check_game_end():
            self.display_board()
            if current_player == "human":
                self.player_turn()
                current_player = "computer"
            else:
                self.ai_turn()
                current_player = "human"
        
        self.display_board()
        print("Game over! The winner is:", self.determine_winner())

    def display_board(self):
        print(f"Current board: Red = {self.marbles['red']}, Blue = {self.marbles['blue']}")

    def get_move_input(self, prompt):
        while True:
            try:
                quantity = int(input(prompt))
                if quantity in [1, 2]:
                    return quantity
                else:
                    print("Invalid input. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def player_turn(self):
        print("Your move:")
        color_choice = input("Enter 'red' or 'blue' to remove marbles: ").strip().lower()
        while color_choice not in ["red", "blue"]:
            color_choice = input("Invalid color. Enter 'red' or 'blue': ").strip().lower()
        marble_count = self.get_move_input("Enter 1 or 2 to remove marbles: ")
        self.marbles[color_choice] -= marble_count
        print(f"You removed {marble_count} {color_choice} marbles.")

    def ai_turn(self):
        print("Computer's move:")
        color_choice = "red" if self.marbles["red"] > 0 else "blue"
        marble_count = min(2, self.marbles[color_choice])
        self.marbles[color_choice] -= marble_count
        print(f"Computer removes {marble_count} {color_choice} marbles.")

    def check_game_end(self):
        return self.marbles["red"] == 0 or self.marbles["blue"] == 0

    def determine_winner(self):
        if self.game_type == "standard":
            return "Human" if self.check_game_end() else "Computer"
        else:
            return "Computer" if self.check_game_end() else "Human"

def main():
    parser = argparse.ArgumentParser(description="Marble Nim Game")
    parser.add_argument("red_count", type=int, help="Number of red marbles")
    parser.add_argument("blue_count", type=int, help="Number of blue marbles")
    parser.add_argument("game_type", choices=["standard", "misere"], help="Game type")
    parser.add_argument("starting_player", choices=["human", "computer"], help="Starting player")
    parser.add_argument("ai_depth", type=int, help="Depth for AI search (not used in this implementation)")

    args = parser.parse_args()

    game = MarbleGame(args.red_count, args.blue_count, args.game_type, args.starting_player, args.ai_depth)
    game.play_game()

if __name__ == "__main__":
    main()
