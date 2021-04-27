#!/usr/bin/env python
import random
from brain_games.gameplay import gameplay


def main():
    information = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_data = {}
    for step in range(3):
        number = random.randint(0, 1000)
        question = f'Question: {number}'
        if number % 2 == 0:
            correct = 'yes'
        else:
            correct = 'no'
        game_data[question] = correct
    gameplay(game_data, information)


if __name__ == '__main__':
    main()
