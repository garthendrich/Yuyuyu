from typing_extensions import Any

from src.globals import Item


def start_quiz(questions: list[Item], screen: Any):
    screen.erase()

    for question in questions:
        screen.addstr(question["prompt"])

    screen.getch()
