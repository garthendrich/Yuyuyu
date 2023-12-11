import curses
from typing_extensions import Any

from src.globals import Item
from src.quiz_proper import start_quiz


def main(screen: Any):
    curses.echo()

    # test quiz proper ---

    items: list[Item] = [
        {"itemType": "identification", "prompt": "What is this question?"},
        {
            "itemType": "multiple choice",
            "prompt": "Choose one bruh",
            "choices": ["1", "one", "isa"],
        },
    ]

    answers = start_quiz(items, screen)

    for answer in answers:
        screen.addstr(str(answer) + "\n")
    screen.getch()

    # [end] test ---


if __name__ == "__main__":
    curses.wrapper(main)
