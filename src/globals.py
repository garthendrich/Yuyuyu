from typing_extensions import Literal, TypedDict


class Identification(TypedDict):
    category: Literal["easy", "average", "difficult"]
    itemType: Literal["identification"]
    prompt: str
    possibleAnswers: list[str]


class MultipleChoice(TypedDict):
    category: Literal["easy", "average", "difficult"]
    itemType: Literal["multiple choice"]
    prompt: str
    choices: list[str]
    answerIndex: int


QuizItem = Identification | MultipleChoice
