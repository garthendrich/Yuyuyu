from curses import window
from typing_extensions import Callable, cast as typecast

from src.utils import displayChoices
from src.globals import Identification, QuizItem, MultipleChoice


def answerIdentification(item: QuizItem, screen: window):
    item = typecast(Identification, item)

    screen.addstr(item["prompt"] + "\n\n👉👉 ")
    answer = screen.getstr().decode()

    return answer


def answerMultipleChoice(item: QuizItem, screen: window):
    item = typecast(MultipleChoice, item)

    categoryDisplay = ""
    if item["category"] == "easy":
        categoryDisplay = "Easy (2 pts)\n\n"
    elif item["category"] == "average":
        categoryDisplay = "Average (3 pts)\n\n"
    elif item["category"] == "difficult":
        categoryDisplay = "Difficult (5 pts)\n\n"

    answerIndex = displayChoices(
        categoryDisplay + item["prompt"], item["choices"], screen
    )

    return answerIndex


answerItemFunctions: dict[str, Callable[[QuizItem, window], str | int]] = {
    "identification": answerIdentification,
    "multiple choice": answerMultipleChoice,
}


def startQuiz(items: list[QuizItem], screen: window) -> list[str | int]:
    screen.erase()
    screen.refresh()

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
