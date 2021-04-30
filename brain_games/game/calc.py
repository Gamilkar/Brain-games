import random


INFORMATION = 'What is the result of the expression?'


def get_data():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 10)
    operator = random.choice(['+', '-', '*'])
    question = f'Question: {first_number} {operator} {second_number}'
    if operator == '-':
        correct = first_number - second_number
    elif operator == '+':
        correct = first_number + second_number
    elif operator == '*':
        correct = first_number * second_number
    return question, str(correct)
