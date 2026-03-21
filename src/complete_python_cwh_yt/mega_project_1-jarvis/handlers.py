# -------------------------------------------------------------------------------------------------------------------------------------------

# handlers.py — Individual command handler functions for the Jarvis assistant.
#
# Each function accepts the minimum context it needs, performs its task, and
# returns a plain string that Jarvis will speak and print.  No I/O is done
# inside these functions — they are pure "process and respond" units.
#
# Commands implemented:
#   get_date()                 — today's date
#   get_time()                 — current time
#   greet(name)                — time-of-day personalised greeting
#   get_joke()                 — random joke via pyjokes
#   search_wikipedia(query)    — 2-sentence Wikipedia summary
#   calculate(expression)      — safe AST-based arithmetic evaluator

# -------------------------------------------------------------------------------------------------------------------------------------------

import ast
import datetime
import operator
from typing import Union

import pyjokes
import wikipedia


# -------------------------------------------------------------------------------------------------------------------------------------------
# Date & Time
# -------------------------------------------------------------------------------------------------------------------------------------------


def get_date() -> str:
    """Return today's date as a human-readable string."""
    today = datetime.date.today()
    return f"Today is {today.strftime('%A, %B %d, %Y')}."


def get_time() -> str:
    """Return the current time as a human-readable string."""
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."


# -------------------------------------------------------------------------------------------------------------------------------------------
# Greeting
# -------------------------------------------------------------------------------------------------------------------------------------------


def greet(name: str) -> str:
    """Return a time-of-day greeting personalised with the user's *name*."""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        period = "morning"
    elif 12 <= hour < 17:
        period = "afternoon"
    elif 17 <= hour < 21:
        period = "evening"
    else:
        period = "night"
    return f"Good {period}, {name}! How can I help you?"


# -------------------------------------------------------------------------------------------------------------------------------------------
# Jokes
# -------------------------------------------------------------------------------------------------------------------------------------------


def get_joke() -> str:
    """Return a random joke from pyjokes."""
    return pyjokes.get_joke()


# -------------------------------------------------------------------------------------------------------------------------------------------
# Wikipedia Search
# -------------------------------------------------------------------------------------------------------------------------------------------


def search_wikipedia(query: str) -> str:
    """Return a 2-sentence Wikipedia summary for *query*.

    Handles disambiguation (too many matches) and page-not-found errors
    gracefully by returning an informative message instead of crashing.

    Args:
        query: The topic to look up.

    Returns:
        A short summary string.
    """
    try:
        # Limit to 2 sentences so the spoken response stays concise.
        summary = wikipedia.summary(query, sentences=2, auto_suggest=True)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        options = ", ".join(e.options[:3])
        return (
            f"'{query}' is ambiguous. Did you mean one of these? {options}. "
            "Please be more specific."
        )
    except wikipedia.exceptions.PageError:
        return f"Sorry, I couldn't find any Wikipedia page for '{query}'."
    except Exception as e:
        return f"Something went wrong while searching Wikipedia: {e}"


# -------------------------------------------------------------------------------------------------------------------------------------------
# Safe arithmetic evaluator
#
# eval() is intentionally avoided.  Instead, we parse the expression into an
# Abstract Syntax Tree (AST) and walk only the node types that correspond to
# safe arithmetic — numbers, unary operators, and binary operators.  Any
# unsupported node (function calls, attribute access, names, etc.) raises a
# ValueError so no arbitrary code can be executed.
# -------------------------------------------------------------------------------------------------------------------------------------------

# Mapping from AST operator types to their Python equivalents.
_BINARY_OPS: dict[type, object] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_UNARY_OPS: dict[type, object] = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _eval_node(node: ast.AST) -> Union[int, float]:
    """Recursively evaluate an AST *node*, raising ValueError for unsafe nodes."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp):
        op_func = _BINARY_OPS.get(type(node.op))
        if op_func is None:
            raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        # Guard against division by zero before calling the operator.
        if isinstance(node.op, (ast.Div, ast.FloorDiv, ast.Mod)) and right == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return op_func(left, right)  # type: ignore[operator]
    if isinstance(node, ast.UnaryOp):
        op_func = _UNARY_OPS.get(type(node.op))
        if op_func is None:
            raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
        return op_func(_eval_node(node.operand))  # type: ignore[operator]
    raise ValueError(f"Unsupported expression element: {type(node).__name__}")


def calculate(expression: str) -> str:
    """Safely evaluate an arithmetic *expression* and return the result string.

    Args:
        expression: A string such as "2 + 3 * 4" or "10 / (2 + 3)".

    Returns:
        A string describing the result, or an error message.
    """
    try:
        tree = ast.parse(expression.strip(), mode="eval")
        result = _eval_node(tree)
        # Format integers without a decimal point for cleaner speech output.
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return f"The answer is {result}."
    except ZeroDivisionError as e:
        return str(e)
    except (ValueError, SyntaxError, TypeError):
        return "Sorry, I couldn't calculate that. Please say a simple arithmetic expression."
