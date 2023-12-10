from typing_extensions import Any, NotRequired, TypedDict


class Item(TypedDict):
    prompt: str
    choices: NotRequired[list[Any]]
