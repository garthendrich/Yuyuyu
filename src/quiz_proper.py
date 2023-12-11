from curses import KEY_DOWN, KEY_ENTER, KEY_UP
from typing_extensions import Any, Callable, cast as typecast

from src.globals import Identification, Item, MultipleChoice


def answerIdentification(item: Item, screen: Any):
    item = typecast(Identification, item)

    screen.addstr(item["prompt"] + "\n\n👉 ")
    answer: str = screen.getstr().decode()

    return answer


def answerMultipleChoice(item: Item, screen: Any):
    item = typecast(MultipleChoice, item)

    answerIndex = 0

    while True:
        screen.addstr(item["prompt"] + "\n\n")

        choices: list[str] = item["choices"]
        for index, choice in enumerate(choices):
            prefix = "👉 " if index == answerIndex else "   "
            screen.addstr(prefix + choice + "\n")

        key: int = screen.getch()
        if key == KEY_UP:
            answerIndex = (answerIndex - 1 + len(choices)) % len(choices)
        elif key == KEY_DOWN:
            answerIndex = (answerIndex + 1) % len(choices)
        elif key == KEY_ENTER or key == 10 or key == 13:
            return answerIndex
            break

        screen.erase()


answerItemFunctions: dict[str, Callable[[Item, Any], str | int]] = {
    "identification": answerIdentification,
    "multiple choice": answerMultipleChoice,
}


def start_quiz(items: list[Item], screen: Any) -> list[str | int]:
    screen.erase()

    answers: list[str | int] = []

    for item in items:
        currentItemType = item["itemType"]

        for itemType in answerItemFunctions:
            if currentItemType == itemType:
                answerItem = answerItemFunctions[itemType]
                answer = answerItem(item, screen)
                answers.append(answer)

        screen.erase()

    return answers
