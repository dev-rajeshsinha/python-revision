"""
╔════════════════════════════════════════════════════════════════════════════╗
║                         NUMBER GUESSING GAME (CLI)                         ║
╚════════════════════════════════════════════════════════════════════════════╝

Overview
--------
- A decorative terminal-based number guessing game with centered boxed UI.
- Supports three difficulty levels: Easy, Medium, and Hard.

Gameplay Rules
--------------
- Each level defines range size, max chances, and score weight.
- Round boundaries are randomized every time while preserving range size.
- Player wins by guessing the secret number within allowed chances.

Scoring
-------
- Win score = level weight × (max_chances - attempts + 1)
- Harder levels have higher weight; faster guesses earn more points.
"""

import os
import random
import shutil
from typing import TypedDict


RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
VERTICAL_BORDER = "║"


class LevelConfig(TypedDict):
    """Typed structure for one difficulty level configuration.

    Attributes:
        name: Human-readable difficulty label.
        lower: Baseline lower bound used to calculate range gap.
        upper: Baseline upper bound used to calculate range gap.
        max_chances: Maximum number of valid in-range guesses allowed.
        score_weight: Difficulty multiplier used in score calculation.
    """

    name: str
    lower: int
    upper: int
    max_chances: int
    score_weight: int


LEVELS: dict[str, LevelConfig] = {
    "1": {
        "name": "Easy",
        "lower": 1,
        "upper": 20,
        "max_chances": 10,
        "score_weight": 1,
    },
    "2": {
        "name": "Medium",
        "lower": 1,
        "upper": 35,
        "max_chances": 7,
        "score_weight": 2,
    },
    "3": {
        "name": "Hard",
        "lower": 1,
        "upper": 50,
        "max_chances": 5,
        "score_weight": 3,
    },
}


def clear_screen() -> None:
    """Clear the terminal screen for a cleaner round-to-round UI transition."""

    os.system("cls" if os.name == "nt" else "clear")


def style(text: str, color: str = "", bold: bool = False) -> str:
    """Wrap text with ANSI color/bold escape codes.

    Args:
        text: Raw text to style.
        color: ANSI color code prefix.
        bold: Whether to add bold styling.

    Returns:
        Styled text with reset code appended.
    """

    bold_code = BOLD if bold else ""
    return f"{bold_code}{color}{text}{RESET}"


def terminal_width() -> int:
    """Return current terminal width with a safe fallback for non-TTY runs."""

    return shutil.get_terminal_size(fallback=(100, 24)).columns


def box_content_width() -> int:
    """Return available content width inside vertical borders.

    Subtracts 2 columns for left and right border characters and enforces a
    minimum width to keep layout readable on narrow terminals.
    """

    return max(terminal_width() - 2, 20)


def fit_text(text: str, width: int) -> str:
    """Fit text into a target width, truncating with ellipsis when required."""

    if len(text) <= width:
        return text
    if width <= 1:
        return text[:width]
    return text[: width - 1] + "…"


def centered_text(text: str, width: int) -> str:
    """Center text within a fixed width after clipping to fit."""

    clipped_text = fit_text(text, width)
    return clipped_text.center(width)


def print_center(text: str, color: str = "", bold: bool = False) -> None:
    """Print one centered line inside the full-width vertical bordered box."""

    content = centered_text(text, box_content_width())
    print(f"{VERTICAL_BORDER}{style(content, color, bold)}{VERTICAL_BORDER}")


def print_blank_line() -> None:
    """Print an empty line while preserving left/right box borders."""

    print(f"{VERTICAL_BORDER}{' ' * box_content_width()}{VERTICAL_BORDER}")


def print_horizontal_rule() -> None:
    """Print a full-width horizontal separator line across the terminal."""

    print(style("─" * terminal_width(), CYAN, bold=True))


def input_center(text: str, color: str = "", bold: bool = False) -> str:
    """Render a centered prompt with horizontal separators and capture input.

    The prompt itself is centered using left-padding only so the input cursor
    appears immediately after the prompt text without trailing whitespace gaps.
    """

    width = terminal_width()
    left_padding = max((width - len(text)) // 2, 0)
    prompt = fit_text(f"{' ' * left_padding}{text}", width)
    # Draw an input section separator before the prompt.
    print_horizontal_rule()
    value = input(style(prompt, color, bold))
    # Move to the next line and close the input section separator.
    print()
    print_horizontal_rule()
    return value


def print_heading(title: str) -> None:
    """Print a decorated heading block with top border and divider line."""

    border_width = box_content_width()
    top_border = f"╔{'═' * border_width}╗"
    divider = f"╠{'═' * border_width}╣"
    print(style(top_border, CYAN, bold=True))
    print_center(title, CYAN, bold=True)
    print(style(divider, CYAN, bold=True))
    print_blank_line()


def get_valid_guess() -> int:
    """Prompt repeatedly until a valid integer guess is entered.

    Returns:
        Parsed integer guess. Range validation is handled elsewhere.
    """

    while True:
        raw_value = input_center("➤ Enter your guess: ", MAGENTA, bold=True).strip()

        # Reject empty values early with a user-friendly message.
        if not raw_value:
            print_center("Please enter a number.", YELLOW)
            print_blank_line()
            continue

        # Accept signed and unsigned integers only.
        if raw_value.startswith("-") and raw_value[1:].isdigit():
            guess = int(raw_value)
        elif raw_value.isdigit():
            guess = int(raw_value)
        else:
            print_center("Invalid input. Enter digits only.", RED)
            print_blank_line()
            continue

        return guess


def choose_level() -> LevelConfig:
    """Display difficulty menu, validate choice, and randomize round boundaries.

    The chosen level keeps its configured range size (gap), but absolute lower
    and upper bounds are randomized for each round.

    Returns:
        A level configuration copy with randomized bounds for this round.
    """

    print_heading("Choose Difficulty Level")
    print_center("1. Easy   (Range size: 20, Chances: 10, Weight: 1)", GREEN)
    print_center("2. Medium (Range size: 35, Chances: 7,  Weight: 2)", YELLOW)
    print_center("3. Hard   (Range size: 50, Chances: 5,  Weight: 3)", RED)
    print_blank_line()

    while True:
        level_choice = input_center(
            "➤ Enter level (1/2/3): ", MAGENTA, bold=True
        ).strip()
        if level_choice in LEVELS:
            # Work on a copy so global level defaults remain unchanged.
            selected_level = LEVELS[level_choice].copy()

            # Preserve each level's range size while shifting the window.
            range_gap = selected_level["upper"] - selected_level["lower"]
            max_start = selected_level["upper"] * 2
            randomized_lower = random.randint(1, max_start)
            selected_level["lower"] = randomized_lower
            selected_level["upper"] = randomized_lower + range_gap
            print_blank_line()
            return selected_level
        print_center("Invalid level. Please enter 1, 2, or 3.", RED)
        print_blank_line()


def play_round(
    lower_limit: int,
    upper_limit: int,
    max_chances: int,
    level_name: str,
    score_weight: int,
) -> int:
    """Run one complete guessing round and return the earned score.

    Args:
        lower_limit: Inclusive lower bound for valid guesses.
        upper_limit: Inclusive upper bound for valid guesses.
        max_chances: Maximum valid in-range attempts allowed.
        level_name: Difficulty label to display.
        score_weight: Difficulty multiplier for score calculation.

    Returns:
        Round score on win, otherwise 0 on loss.
    """

    # Choose secret number inside the randomized bounds for this round.
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    print_heading("Number Guessing Game")
    print_center(f"Level: {level_name}", CYAN, bold=True)
    print_center(f"I picked a number between {lower_limit} and {upper_limit}.", CYAN)
    print_center(f"You have {max_chances} chance(s).", CYAN)
    print_blank_line()

    while attempts < max_chances:
        # Parse numeric input first; range checks happen below.
        guess = get_valid_guess()
        print_blank_line()

        # Ignore out-of-range guesses without consuming chances.
        if not lower_limit <= guess <= upper_limit:
            print_center(
                f"Out of range! Pick a number between {lower_limit} and {upper_limit}.",
                RED,
            )
            print_blank_line()
            continue

        # Count only valid in-range guesses as attempts.
        attempts += 1
        remaining_chances = max_chances - attempts

        # Win branch: compute efficiency-based score and end round.
        if guess == secret_number:
            efficiency_score = max_chances - attempts + 1
            round_score = score_weight * efficiency_score
            print_center(
                f"Correct! You guessed it in {attempts} attempt(s).",
                GREEN,
                bold=True,
            )
            print_center(
                "Score: "
                f"{score_weight} × ({max_chances} - {attempts} + 1) "
                f"= {score_weight} × {efficiency_score} = {round_score}",
                MAGENTA,
            )
            print_blank_line()
            return round_score

        # Final miss: skip high/low hint and show loss summary after loop.
        if remaining_chances == 0:
            break

        # Non-final miss: provide directional hint and remaining chances.
        if guess < secret_number:
            print_center("Too low. Try again!", YELLOW)
            print_center(f"Chance(s) left: {remaining_chances}", CYAN)
            print_blank_line()
        else:
            print_center("Too high. Try again!", YELLOW)
            print_center(f"Chance(s) left: {remaining_chances}", CYAN)
            print_blank_line()

    print_center("No chances left. Better luck next time!", RED, bold=True)
    print_center(f"The correct number was {secret_number}.", YELLOW)
    print_blank_line()
    return 0


def ask_to_play_again() -> bool:
    """Ask replay confirmation until a valid yes/no response is provided."""

    while True:
        choice = (
            input_center("➤ Play again? (y/n): ", MAGENTA, bold=True).strip().lower()
        )
        if choice in {"y", "yes"}:
            print_blank_line()
            return True
        if choice in {"n", "no"}:
            print_blank_line()
            return False
        print_center("Please type 'y' or 'n'.", RED)
        print_blank_line()


def main() -> None:
    """Program entry point: run game loop, aggregate score, and exit cleanly."""

    # Initial UI setup.
    clear_screen()
    print_heading("Welcome to the Number Guessing Game")
    total_score = 0

    while True:
        # 1) Choose level and randomized bounds for the next round.
        selected_level = choose_level()

        # 2) Clear menu screen before starting gameplay view.
        clear_screen()

        # 3) Run one round and accumulate the returned score.
        round_score = play_round(
            lower_limit=selected_level["lower"],
            upper_limit=selected_level["upper"],
            max_chances=selected_level["max_chances"],
            level_name=selected_level["name"],
            score_weight=selected_level["score_weight"],
        )
        total_score += round_score
        print_center(f"Total score: {total_score}", CYAN, bold=True)
        print_blank_line()

        # 4) Continue or finish based on player confirmation.
        wants_to_play_again = ask_to_play_again()
        if wants_to_play_again:
            clear_screen()
            continue

        # 5) Final summary and visual closing border.
        print_center(
            f"Thanks for playing. Final score: {total_score}", GREEN, bold=True
        )
        print_blank_line()
        print_horizontal_rule()
        break


if __name__ == "__main__":
    main()
