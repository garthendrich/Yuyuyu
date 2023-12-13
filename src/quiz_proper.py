from typing_extensions import Any, Callable, cast as typecast

from src.choices import displayChoices
from src.globals import Identification, Item, MultipleChoice


def answerIdentification(item: Item, screen: Any):
    item = typecast(Identification, item)

    screen.addstr(item["prompt"] + "\n\n👉 ")
    answer: str = screen.getstr().decode()

    return answer


def answerMultipleChoice(item: Item, screen: Any):
    item = typecast(MultipleChoice, item)

    answerIndex = displayChoices(item["prompt"], item["choices"], screen)

    return answerIndex


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
