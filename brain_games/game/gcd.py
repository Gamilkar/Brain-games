import random


INFORMATION = 'Find the greatest common divisor of given numbers.'


def get_data():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 10)
    question = f'Question: {first_number} {second_number}'
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    correct = first_number + second_number
    return question, str(correct)
