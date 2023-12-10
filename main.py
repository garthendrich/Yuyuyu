from curses import wrapper
from typing_extensions import Any

from src.globals import Item
from src.quiz_proper import start_quiz


def main(screen: Any):
    items: list[Item] = [{"prompt": "What is this question?"}]
    start_quiz(items, screen)


if __name__ == "__main__":
    wrapper(main)
