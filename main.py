import curses
from typing_extensions import Any

from src.choices import displayChoices
from src.client import proceedAsClient
from src.server import proceedAsServer


def main(screen: Any):
    curses.echo()

    choiceIndex = displayChoices("Yuyuyu", ["Host the test", "Take the test"], screen)

    if choiceIndex == 0:
        proceedAsServer()
    else:
        proceedAsClient()

    # test quiz proper ---

    # items: list[Item] = [
    #     {"itemType": "identification", "prompt": "What is this question?"},
    #     {
    #         "itemType": "multiple choice",
    #         "prompt": "Choose one bruh",
    #         "choices": ["1", "one", "isa"],
    #     },
    # ]

    # answers = start_quiz(items, screen)

    # for answer in answers:
    #     screen.addstr(str(answer) + "\n")
    # screen.getch()

    # [end] test ---


if __name__ == "__main__":
    curses.wrapper(main)
