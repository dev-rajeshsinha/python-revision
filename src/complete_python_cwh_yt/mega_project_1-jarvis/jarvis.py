# -------------------------------------------------------------------------------------------------------------------------------------------

# jarvis.py — The Jarvis class: command matching, dispatch, and the main loop.
#
# Jarvis stores the user's name, normalises every incoming query, maps it to
# a command token via keyword matching, dispatches to the appropriate handler
# in handlers.py, and returns the response string.  Voice I/O is handled by
# the caller (main.py) so this class stays testable without audio hardware.

# -------------------------------------------------------------------------------------------------------------------------------------------

import re

from handlers import (
    calculate,
    get_date,
    get_joke,
    get_time,
    greet,
    search_wikipedia,
)
import voice


# -------------------------------------------------------------------------------------------------------------------------------------------
# Jarvis
# -------------------------------------------------------------------------------------------------------------------------------------------


class Jarvis:
    """A voice-enabled virtual assistant that responds to predefined commands.

    Attributes:
        name: The user's name, used to personalise responses.
    """

    # Keywords that map spoken/typed phrases to command tokens.
    _COMMAND_KEYWORDS: dict[str, list[str]] = {
        "date": ["date", "today", "day", "what day"],
        "time": ["time", "clock", "hour", "what time"],
        "greet": [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
            "good night",
        ],
        "joke": ["joke", "funny", "laugh", "make me laugh", "tell me a joke"],
        "wiki": [
            "search",
            "wikipedia",
            "wiki",
            "tell me about",
            "what is",
            "who is",
            "what are",
        ],
        "math": [],  # Detected by pattern, not keywords — see _match_command()
    }

    def __init__(self, name: str) -> None:
        """Initialise Jarvis with the user's *name*."""
        self.name = name

    # -----------------------------------------------------------------------
    # Private helpers
    # -----------------------------------------------------------------------

    def _match_command(self, query: str) -> str:
        """Map a normalised *query* to a command token.

        Checks keywords in priority order.  Falls back to a heuristic for
        arithmetic expressions (digits + operators) before returning "unknown".

        Args:
            query: Lower-case, stripped input string.

        Returns:
            A command token: "date" | "time" | "greet" | "joke" |
            "wiki" | "math" | "unknown".
        """
        for command, keywords in self._COMMAND_KEYWORDS.items():
            for keyword in keywords:
                if keyword in query:
                    return command

        # Arithmetic heuristic: contains digits and at least one operator.
        if re.search(r"\d", query) and re.search(r"[+\-*/^]", query):
            return "math"

        return "unknown"

    def _extract_wiki_query(self, query: str) -> str:
        """Strip trigger keywords from *query* to get the bare search term."""
        triggers = [
            "tell me about",
            "search for",
            "search",
            "wikipedia",
            "wiki",
            "what is",
            "what are",
            "who is",
        ]
        result = query
        for trigger in triggers:
            result = result.replace(trigger, "").strip()
        return result if result else query

    def _extract_math_expression(self, query: str) -> str:
        """Extract only the arithmetic characters from *query*."""
        # Keep digits, operators, spaces, parentheses, and dot for decimals.
        return re.sub(r"[^0-9+\-*/().^ ]", "", query).strip()

    def _handle(self, command: str, query: str) -> str:
        """Dispatch *command* to the correct handler and return the response.

        Args:
            command: Token returned by _match_command().
            query:   Original normalised query (used to extract sub-terms).

        Returns:
            A human-readable response string.
        """
        if command == "date":
            return get_date()
        if command == "time":
            return get_time()
        if command == "greet":
            return greet(self.name)
        if command == "joke":
            return get_joke()
        if command == "wiki":
            topic = self._extract_wiki_query(query)
            if not topic:
                return "What would you like me to search for?"
            return search_wikipedia(topic)
        if command == "math":
            expression = self._extract_math_expression(query)
            if not expression:
                return "I couldn't find a valid expression to calculate."
            return calculate(expression)
        # "unknown" fallback
        return (
            f"I'm sorry, {self.name}, I didn't understand that. "
            "You can ask me about the date, time, a joke, search Wikipedia, "
            "or do a quick calculation."
        )

    # -----------------------------------------------------------------------
    # Public API
    # -----------------------------------------------------------------------

    def process(self, query: str) -> str:
        """Normalise *query*, match a command, dispatch, and return response.

        Args:
            query: Raw text from voice recognition or keyboard input.

        Returns:
            Jarvis's response as a plain string.
        """
        normalised = query.lower().strip()
        command = self._match_command(normalised)
        return self._handle(command, normalised)

    def run(self) -> None:
        """Start the main listen → respond loop.

        Listens for voice input, processes it, and speaks the response.
        The loop exits when the user says or types "bye", "exit", or "quit".
        """
        voice.speak(
            f"Hello {self.name}! I'm Jarvis, your personal assistant. "
            "How can I help you today?"
        )

        while True:
            query = voice.listen()

            # Fallback to typed input if microphone is unavailable.
            if query is None:
                try:
                    query = input("You (type): ").lower().strip()
                except (EOFError, KeyboardInterrupt):
                    break
                if not query:
                    continue

            # Exit commands.
            if query in {"bye", "exit", "quit", "goodbye", "see you"}:
                voice.speak(f"Goodbye, {self.name}! Have a great day.")
                break

            response = self.process(query)
            voice.speak(response)
