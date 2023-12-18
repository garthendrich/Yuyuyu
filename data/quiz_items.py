from src.globals import QuizItem


items: list[QuizItem] = [
    {
        "category": "easy",
        "itemType": "identification",
        "prompt": "______ is a list of instructions, together with any fixed information required to carry out instructions.",
        "possibleAnswers": ["Program", "program"],
    },

    {
        "category": "easy",
        "itemType": "identification",
        "prompt": "Number 68 in the decimal system can be expressed in the binary system as what number?",
        "possibleAnswers": ["1000100"],
    },
    
    {
        "category": "easy",
        "itemType": "identification",
        "prompt": "In creating flowcharts, this shape indicates the start or end of a program. ",
        "possibleAnswers": ["Oval", "oval"],
    },

    {
        "category": "easy",
        "itemType": "multiple choice",
        "prompt": "This shape indicates “process” in flowcharts.", 
        "choices": ["Rectangle", "Parallelogram", "Arrows", "Oval"],
        "answerIndex": 0,
    },

    {
        "category": "easy",
        "itemType": "identification",
        "prompt": "Given that a = “JAYSIE”, what is a[2]?",
        "possibleAnswers": ["Y"],
    },

    {
        "category": "average",
        "itemType": "identification",
        "prompt": "This refers to the duration it takes for an algorithm to execute a specific sequence of instructions.",
        "possibleAnswers": ["Time Complexity", "time complexity", "Time complexity"],
    },

    {
        "category": "average",
        "itemType": "multiple choice",
        "prompt": "An array allows you to store a group of items of different data type together in memory.",
        "choices": ["True", "False"],
        "answerIndex": 1,
    },

    {
        "category": "average",
        "itemType": "identification",
        "prompt": "This is the use of experiments with random numbers to evaluate mathematical expressions that may be definite integrals, systems of equations or more complicated mathematical models.",
        "possibleAnswers": ["Monte Carlo Simulation", "Monte carlo Simulation", "Monte Carlo simulation", "monte carlo simulation"],
    },

    
    {
        "category": "average",
        "itemType": "identification",
        "prompt": "What error is manifested by the following code: \n\nimport math\nprint(math.exp(9999))",
        "possibleAnswers": ["Overflow Error", "Overflow error", "overflow error", "Overflow", "overflow"],
    },

    {
        "category": "difficult",
        "itemType": "multiple choice",
        "prompt": "Rewrite P(x)=3x^3 +2x^2 -6x +7 using Horner's Method. Equate the manipulated expression to P(x).",
        "choices": ["P(x)=7+x(-6+x(2+3x))", "P(x)=((3x+2)-6)x+7", "P(x)=7+(-6+x(2+3x))", "P(x)=P(x)=(3x+2)x-6x+7"],
        "answerIndex": 0,
    },

    
    {
        "category": "difficult",
        "itemType": "identification",
        "prompt": "Find L2 or Euclidean norm of the vector x = (1,2,4,2).",
        "possibleAnswers": ["5", "5.0"],
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
