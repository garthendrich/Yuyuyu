from curses import KEY_DOWN, KEY_ENTER, KEY_UP, window
from typing_extensions import Literal


def displayChoices(prompt: str, choices: list[str], screen: window):
    choiceIndex = 0

    while True:
        screen.addstr(prompt + "\n\n")

        for index, choice in enumerate(choices):
            prefix = "👉👉 " if index == choiceIndex else "     "
            screen.addstr(prefix + choice)
            if index == choiceIndex:
                screen.addstr(" 👈👈")
            screen.addstr("\n")

        key: int = screen.getch()
        if key == KEY_UP:
            choiceIndex = (choiceIndex - 1 + len(choices)) % len(choices)
        elif key == KEY_DOWN:
            choiceIndex = (choiceIndex + 1) % len(choices)
        elif key == KEY_ENTER or key == 10 or key == 13:
            return choiceIndex

        screen.clear()


def getScoreByCategory(category: Literal["easy", "average", "difficult"]):
    if category == "easy":
        return 2
    elif category == "average":
        return 3
    elif category == "difficult":
        return 5
