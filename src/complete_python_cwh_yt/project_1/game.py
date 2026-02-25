# -------------------------------------------------------------------------------------------------------------------------------------------

# We need to build a Snake Water Gun game in Python. The rules of the game are as follows:
# 1. Snake drinks water, so snake wins.
# 2. Gun shoots snake, so gun wins.
# 3. Water douses gun, so water wins.
# 4. If both players choose the same option, it's a tie.
# The game should be played between the user and the computer. The user will input their choice, and the computer will randomly select its choice. The game will then determine the winner based on the rules mentioned above.

# -------------------------------------------------------------------------------------------------------------------------------------------

import random
import os


def show_intro_and_rules():
    """Display a short game introduction and the Snake-Water-Gun rules."""
    print("\nWelcome to Snake Water Gun!")
    print(
        "This is a quick strategy game where you play against the computer "
        "for a fixed number of moves."
    )
    print("\nRules:")
    print("1. Snake drinks water, so snake wins.")
    print("2. Gun shoots snake, so gun wins.")
    print("3. Water douses gun, so water wins.")
    print("4. If both choices are same, the move is a tie.")


def clear_screen():
    """Clear terminal output for Windows and Unix-like systems."""
    os.system("cls" if os.name == "nt" else "clear")


def get_player_name():
    """Read, validate, and return a non-empty player name."""
    while True:
        name = input("\nEnter your player name: ").strip()
        if name:
            return name
        print("Player name cannot be empty. Please try again.")


def get_level_details(player_name, session_stats):
    """Return selected level and move count, or (None, None) to exit."""
    # Harder levels have fewer moves.
    level_map = {
        "easy": 7,
        "medium": 5,
        "hard": 3,
    }

    while True:
        clear_screen()
        show_intro_and_rules()

        # Accept level choice, on-demand score view, or exit request.
        level = (
            input(
                "\nChoose level (easy/medium/hard), type 'score' to view session score, or 'exit': "
            )
            .strip()
            .lower()
        )
        # Signal caller to end the full game session.
        if level == "exit":
            return None, None
        # Show cumulative score without starting a new game.
        if level == "score":
            show_session_scoreboard(player_name, session_stats)
            continue
        # Return valid level and its configured move limit.
        if level in level_map:
            return level, level_map[level]
        print("Invalid level. Please choose easy, medium, or hard.")


def decide_winner(user_choice, computer_choice):
    """Evaluate one move and return 'player', 'computer', or 'tie'."""
    # Same choice means no one wins the move.
    if user_choice == computer_choice:
        return "tie"

    # Explicit winning combinations for the player.
    if (
        (user_choice == "snake" and computer_choice == "water")
        or (user_choice == "water" and computer_choice == "gun")
        or (user_choice == "gun" and computer_choice == "snake")
    ):
        return "player"

    # Any remaining non-tie case is a computer win.
    return "computer"


def play_game(player_name, level, total_moves):
    """Run one game session for selected level and return game winner."""
    # Available moves in the game.
    options = ("snake", "water", "gun")
    # Per-game score counters reset for every new game.
    player_score = 0
    computer_score = 0
    tie_score = 0

    print(
        f"\nStarting game for {player_name} | Level: {level.title()} | Moves: {total_moves}"
    )

    move = 1
    while move <= total_moves:
        # Show move count and current per-game score in one line.
        print(
            f"\nMove {move}/{total_moves} | Score -> {player_name}: {player_score}, Computer: {computer_score}, Ties: {tie_score}"
        )
        user_choice = (
            input("Enter your choice (snake/water/gun) or type 'exit': ")
            .strip()
            .lower()
        )

        if user_choice == "exit":
            # Allow user to leave the current game before all moves are played.
            print("Exiting current game early.")
            break

        # Invalid input does not consume a move.
        if user_choice not in options:
            print("Invalid choice! Please choose snake, water, or gun.")
            continue

        # Computer randomly picks one of the valid moves.
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)
        # Update per-game score based on move outcome.
        if result == "tie":
            tie_score += 1
            print("It's a tie!")
        elif result == "player":
            player_score += 1
            print(f"{player_name} wins this move!")
        else:
            computer_score += 1
            print("Computer wins this move!")

        move += 1

    # Final score and winner are decided from per-game counters.
    print("\nGame Over")
    print(f"Final score -> {player_name}: {player_score}, Computer: {computer_score}")

    if player_score > computer_score:
        print(f"{player_name} wins the game!")
        return "player"
    elif computer_score > player_score:
        print("Computer wins the game!")
        return "computer"
    else:
        print("The game is a tie!")
        return "tie"


def show_session_scoreboard(player_name, session_stats):
    """Print cumulative score for the current program session."""
    print("\nSession Scoreboard")
    print(f"Games played: {session_stats['played']}")
    print(f"{player_name} won: {session_stats['player_wins']}")
    print(f"Computer won: {session_stats['computer_wins']}")
    print(f"Tied games: {session_stats['ties']}")


def snake_water_gun():
    """Program entry: handle setup, repeated games, and session scoring."""
    clear_screen()
    show_intro_and_rules()
    player_name = get_player_name()
    # Session score persists across multiple games in one program run.
    session_stats = {
        "played": 0,
        "player_wins": 0,
        "computer_wins": 0,
        "ties": 0,
    }

    while True:
        # Ask for level before each new game.
        level, total_moves = get_level_details(player_name, session_stats)
        if level is None:
            print(f"\nThanks for playing, {player_name}!")
            break

        clear_screen()
        show_intro_and_rules()

        game_result = play_game(player_name, level, total_moves)
        # Update cumulative session statistics after each game.
        session_stats["played"] += 1
        if game_result == "player":
            session_stats["player_wins"] += 1
        elif game_result == "computer":
            session_stats["computer_wins"] += 1
        else:
            session_stats["ties"] += 1

        while True:
            # Replay menu with on-demand session scoreboard support.
            play_again = (
                input(
                    "\nDo you want to play another game? (yes/no) or type 'score' to view session score: "
                )
                .strip()
                .lower()
            )
            if play_again == "score":
                show_session_scoreboard(player_name, session_stats)
                continue
            if play_again == "yes":
                break
            if play_again == "no":
                print(f"\nThanks for playing, {player_name}!")
                return
            print("Invalid input. Please type yes, no, or score.")


if __name__ == "__main__":
    snake_water_gun()
