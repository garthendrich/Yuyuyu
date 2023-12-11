from typing_extensions import Literal, TypedDict


class Identification(TypedDict):
    itemType: Literal["identification"]
    prompt: str


class MultipleChoice(TypedDict):
    itemType: Literal["multiple choice"]
    prompt: str
    choices: list[str]


Item = Identification | MultipleChoice
