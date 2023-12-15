from src.globals import QuizItem


items: list[QuizItem] = [
    {
        "itemType": "identification",
        "prompt": "What is this question?",
        "possibleAnswers": ["hindi", "ko", "alam"],
    },
    {
        "itemType": "multiple choice",
        "prompt": "Choose one bruh",
        "choices": ["1", "one", "isa"],
        "answerIndex": 2,
    },
]


quizItemsWithoutAnswers = [
    {
        key: value
        for key, value in quizItem.items()
        if key not in ["possibleAnswers", "answerIndex"]
    }
    for quizItem in items
]
