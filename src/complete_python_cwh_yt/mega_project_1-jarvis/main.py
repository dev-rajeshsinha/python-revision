# -------------------------------------------------------------------------------------------------------------------------------------------

# main.py — Entry point for the Jarvis virtual assistant.
#
# Workflow:
#   1. Jarvis speaks a welcome prompt asking for the user's name.
#   2. The user says their name (or types it if the mic is unavailable).
#   3. A Jarvis instance is created with that name.
#   4. jarvis.run() starts the voice-in / voice-out interaction loop.
#
# Run with:
#   python main.py

# -------------------------------------------------------------------------------------------------------------------------------------------

import sys

# Ensure the package directory is importable when running the file directly.
import os

sys.path.insert(0, os.path.dirname(__file__))

from jarvis import Jarvis
import voice


# -------------------------------------------------------------------------------------------------------------------------------------------
# Name acquisition helpers
# -------------------------------------------------------------------------------------------------------------------------------------------


def _ask_for_name() -> str:
    """Prompt the user for their name via voice, falling back to keyboard.

    Tries up to three times to capture a non-empty name via the microphone.
    If all voice attempts fail (no mic, no network, etc.) it silently falls
    back to a `input()` prompt so Jarvis still works in text-only mode.

    Returns:
        The user's name, cleaned and title-cased.
    """
    voice.speak("Hello! What is your name?")

    # Attempt to capture the name via microphone up to 3 times.
    for attempt in range(3):
        name = voice.listen()
        if name:
            # Clean common filler phrases like "my name is ..." or "i am ..."
            for filler in ("my name is", "i am", "i'm", "call me", "it's", "its"):
                name = name.replace(filler, "").strip()
            if name:
                return name.title()
        if attempt < 2:
            voice.speak(
                "Sorry, I didn't catch that. Could you please say your name again?"
            )

    # Fallback: typed input.
    print("\n[Microphone input unavailable — switching to keyboard input.]")
    while True:
        name = input("Please type your name: ").strip()
        if name:
            return name.title()
        print("Name cannot be empty. Please try again.")


# -------------------------------------------------------------------------------------------------------------------------------------------
# Entry point
# -------------------------------------------------------------------------------------------------------------------------------------------


def main() -> None:
    """Initialise and launch the Jarvis assistant."""
    print("=" * 60)
    print("         JARVIS — Your Personal Voice Assistant")
    print("=" * 60)

    try:
        name = _ask_for_name()
        assistant = Jarvis(name)
        assistant.run()
    except KeyboardInterrupt:
        print("\n\n[Interrupted by user. Goodbye!]")
    finally:
        print("\n[Jarvis has shut down.]")


if __name__ == "__main__":
    main()
