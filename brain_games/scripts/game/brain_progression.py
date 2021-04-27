#!/usr/bin/env python
import random
from brain_games.gameplay import gameplay


def main():
    information = 'What number is missing in the progression?'
    game_data = {}
    for step in range(3):
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
        game_data[question] = str(correct)
    gameplay(game_data, information)


if __name__ == '__main__':
    main()
