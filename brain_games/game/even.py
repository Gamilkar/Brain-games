import random


INFORMATION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_data():
    number = random.randint(0, 1000)
    question = f'Question: {number}'
    if number % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    return question, correct
