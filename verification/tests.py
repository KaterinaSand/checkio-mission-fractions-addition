"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ((2, 3), (2, 3)),
            "answer": "1 and 1/3"
        },
        {
            "input": ((1, 3), (1, 3)),
            "answer": '2/3'
        }
    ],
    "Extra": [
        {
            "input": ((1, 3), (1, 3), (1, 3)),
            "answer": 1
        },
        {
            "input": ((2, 1), (3, 1), (4, 2), (5, 1)),
            "answer": 12
        }
    ]
}
