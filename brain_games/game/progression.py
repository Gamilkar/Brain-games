import random


INFORMATION = 'What number is missing in the progression?'


def get_data():
    sequence = ''
    sequence_len = random.randint(5, 10)
    x = random.randint(0, sequence_len - 1)
    a = random.randint(1, 10)
    d = random.randint(1, 10)
    for number in range(sequence_len):
        if number == x:
            sequence += '.. '
            correct = a
        else:
            sequence += str(a) + ' '
        a += d
    question = f'Question: {sequence}'
    return question, str(correct)
